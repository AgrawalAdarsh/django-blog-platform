from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post
from .serializers import PostSerializer
from .permissions import IsWriterOrAdmin, IsOwnerOrAdmin


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()   # ✅ REQUIRED
    serializer_class = PostSerializer
    search_fields = ['title', 'content', 'tags']

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated and user.role == 'admin':
            return Post.objects.all()

        return Post.objects.filter(status='published')

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]

        return [IsAuthenticated(), IsWriterOrAdmin(), IsOwnerOrAdmin()]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
