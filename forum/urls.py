from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.forum_home, name='forum'),
    path('create/', views.CreateThread.as_view(), name='create-thread'),
    path('list/', views.ThreadList.as_view(), name='list-thread'),
    path('api/', include(('forum.api.urls', 'forum.api'), namespace='forum-api')),
]
