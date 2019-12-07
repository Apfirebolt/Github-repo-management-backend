from django.urls import path, include
from django.views.generic import TemplateView
from github import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='github/home.html')),
    path('api/', include(('github.api.urls', 'github.api'), namespace='github-api')),
    path('search_user', views.search_user, name='search-user'),
    path('search_repo', views.search_repo, name='search-repo'),
    path('search_topic', views.search_topic, name='search-topic'),
    path('saved_users', views.RepoUserListView.as_view(), name='list-user'),
    path('saved_topics', views.RepoTopicListView.as_view(), name='saved-topics')
]