from django.urls import path, include
from .views import BlogPostList
from rest_framework import routers

router = routers.DefaultRouter()
router.register('BlogPost', BlogPostList)

urlpatterns = [
    path('api/', include(router.urls))
]
