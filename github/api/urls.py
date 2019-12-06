from django.urls import path
from . import views

urlpatterns = [
    path('list', views.RepoListView.as_view(), name='repo-list'),
    path('create', views.RepoCreateView.as_view(), name='repo-create'),
]