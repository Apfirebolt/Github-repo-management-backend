from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView
from . forms import UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from github.models import RepoModel


class RegisterForm(FormView):
    form_class = UserModelForm
    template_name = 'accounts/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(reverse('accounts:login'))

    def form_invalid(self, form):
        print('Form is invalid!', form.errors)
        return HttpResponseRedirect(reverse('home'))


def accounts_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
      login(request, user)
      return HttpResponseRedirect(reverse('home'))

    else:
      print('User not found')
      return HttpResponseRedirect(reverse('accounts:login'))

  else:
    return render(request, 'accounts/login.html', {})


class RepoList(LoginRequiredMixin, ListView):
    model = RepoModel
    template_name = 'accounts/dashboard.html'
    context_object_name = 'my_saved_repos'

    def get_queryset(self):
        queryset = RepoModel.objects.filter(owner=self.request.user)
        return queryset








