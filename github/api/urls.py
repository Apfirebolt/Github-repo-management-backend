from django.urls import path
from . import views

urlpatterns = [
    path('list', views.RepoListView.as_view(), name='repo-list'),
    path('create', views.RepoCreateView.as_view(), name='repo-create'),
    path('delete/<int:pk>', views.RepoDeleteView.as_view(), name='repo-delete'),
]