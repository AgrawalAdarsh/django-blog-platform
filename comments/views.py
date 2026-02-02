from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsOwnerComment


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()   # ✅ ADD THIS LINE
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerComment]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
