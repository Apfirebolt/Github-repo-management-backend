from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from rest_framework import generics
from rest_framework import permissions
from . serializers import BlogPostSerializer, BlogCategorySerializer
from blog.models import BlogPost, BlogCategory


class APITweet(TemplateView):

    template_name = 'gallery/test_api.html'


class BlogPostListAPIView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return BlogPost.objects.all()


class BlogPostCreateAPIView(generics.CreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.IsAuthenticated,)


class BlogCategoryAPIView(generics.ListAPIView):
    serializer_class = BlogCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def dispatch(self, request, *args, **kwargs):
        context = super(BlogCategoryAPIView, self).dispatch(request, **kwargs)
        print('Dispatch method was called : ', context)
        return context

    def get_queryset(self):
        return BlogCategory.objects.all()


class BlogCategoryDelete(generics.DestroyAPIView):
    serializer_class = BlogCategorySerializer
    queryset = BlogCategory.objects.all()


class BlogPostDelete(generics.DestroyAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

