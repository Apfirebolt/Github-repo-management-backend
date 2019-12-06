from django.shortcuts import render
from django.http import HttpResponse


def search_user(request):
    return render(request, 'github/search_user.html', {})


def search_repo(request):
  return render(request, 'github/search_repo.html', {})


def search_topic(request):
  return render(request, 'github/search_topic.html', {})

