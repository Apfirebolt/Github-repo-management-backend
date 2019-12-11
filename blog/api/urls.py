from django.urls import path, include
from . import views


urlpatterns = [
    path('blog-list/', views.BlogCategoryAPIView.as_view(), name='blog-cat-api'),
    path('post-list/', views.BlogPostListAPIView.as_view(), name='blog-post-api'),
    path('blog-delete/<int:pk>', views.BlogCategoryDelete.as_view(), name='blog-delete'),
    path('post-delete/<int:pk>', views.BlogPostDelete.as_view(), name='post-delete'),
    path('post-create/', views.BlogPostCreateAPIView.as_view(), name='blog-post-create-api'),
]