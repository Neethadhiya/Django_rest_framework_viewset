from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostsViewsets

router = DefaultRouter()
router.register(r'posts', PostsViewsets, basename = 'post')

urlpatterns = [
    path('', include(router.urls))
]
