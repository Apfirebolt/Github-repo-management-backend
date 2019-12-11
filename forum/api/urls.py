from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ThreadListView.as_view(), name='thread-list'),
    path('create', views.ThreadCreateView.as_view(), name='thread-create'),
]