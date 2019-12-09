from django.urls import path
from . import views

urlpatterns = [
    path('list', views.RepoListView.as_view(), name='repo-list'),
    path('create', views.RepoCreateView.as_view(), name='repo-create'),
    path('delete/<int:pk>', views.RepoDeleteView.as_view(), name='repo-delete'),
    path('star/<int:pk>', views.RepoStarView.as_view(), name='repo-star'),
    path('user', views.RepoUserModelCreate.as_view(), name='user-create'),
    path('user_list', views.RepoUserListView.as_view(), name='user-list'),
    path('topic', views.RepoTopicCreateView.as_view(), name='topic-create'),
    path('topic_list', views.RepoTopicListView.as_view(), name='topic-list'),
    path('edit_description/<int:pk>', views.RepoTopicDescriptionEdit.as_view(), name='edit-description'),
]