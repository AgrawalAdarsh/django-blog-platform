from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet
from comments.views import CommentViewSet
from users.views import RegisterView
from django.http import HttpResponse

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('comments', CommentViewSet, basename='comments')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/', include(router.urls)),
    path('', lambda request: HttpResponse("Blog API is running 🚀")),
    ]

def home(request):
    return HttpResponse("Frontend running")
