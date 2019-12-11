from rest_framework import serializers
from blog.models import BlogPost, BlogCategory


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'blog_image']


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['title', 'owner', 'category']

