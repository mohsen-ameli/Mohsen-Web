from django.shortcuts import render
from rest_framework import viewsets
from blog.models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostList(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

