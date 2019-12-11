from django import forms
from . models import BlogCategory, BlogPost


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogCategory

        fields = ['title', 'category']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost

        fields = ['title', 'body', 'blog_image']