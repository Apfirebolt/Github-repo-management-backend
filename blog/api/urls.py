from django.urls import path, include
from . import views


urlpatterns = [
    path('blog-list/', views.BlogCategoryAPIView.as_view(), name='blog-cat-api'),
    path('post-list/', views.BlogPostListAPIView.as_view(), name='blog-post-api'),
    path('post-create/', views.BlogPostCreateAPIView.as_view(), name='blog-post-create-api'),
]