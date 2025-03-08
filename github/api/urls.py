from django.urls import path
from . import views

urlpatterns = [
    path('list', views.RepoListView.as_view(), name='repo-list'),
    path('create', views.RepoCreateView.as_view(), name='repo-create'),
    path('delete/<int:pk>', views.RepoDeleteView.as_view(), name='repo-delete'),
    path('star/<int:pk>', views.RepoStarView.as_view(), name='repo-star'),
    path('user', views.RepoUserModelCreate.as_view(), name='user-create'),
    path('user/<int:pk>', views.RepoUserModelDelete.as_view(), name='user-delete'),
    path('user_list', views.RepoUserListView.as_view(), name='user-list'),
]