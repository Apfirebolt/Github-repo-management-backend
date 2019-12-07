from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from github.models import RepoUserModel, RepoTopicModel
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def search_user(request):
    return render(request, 'github/search_user.html', {})


def search_repo(request):
  return render(request, 'github/search_repo.html', {})


def search_topic(request):
  return render(request, 'github/search_topic.html', {})


class RepoUserListView(LoginRequiredMixin, ListView):
    model = RepoUserModel
    template_name = 'github/list_user.html'
    context_object_name = 'saved_profiles'

    def get_queryset(self):
        queryset = RepoUserModel.objects.filter(owner=self.request.user)
        return queryset


class RepoTopicListView(LoginRequiredMixin, ListView):
    model = RepoTopicModel
    template_name = 'github/list_topics.html'
    context_object_name = 'saved_topics'

    def get_queryset(self):
        queryset = RepoTopicModel.objects.filter(owner=self.request.user)
        messages.add_message(self.request, messages.INFO, 'Hello world.')
        return queryset
