from django.shortcuts import render
from django.views.generic import TemplateView, FormView, ListView, UpdateView
from django.template import RequestContext
from . forms import UserModelForm, SettingsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from github.models import RepoModel
from accounts.models import CustomUser


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


class EditAccountSettings(UpdateView):
    form_class = SettingsForm
    template_name = 'accounts/settings.html'
    success_url = '/'
    model = CustomUser

    def form_valid(self, form):
        user = form.save(commit=False)
        user.profile_image = form.cleaned_data['profile_image']
        user.about_me = form.cleaned_data['about_me']
        user.save()
        return HttpResponseRedirect(reverse('accounts:login'))

    def form_invalid(self, form):
        print('Form is invalid!', form.errors)
        return HttpResponseRedirect(reverse('home'))

    def get_object(self, queryset=None):
        """ To check if the user is the owner of the object """
        obj = super(EditAccountSettings, self).get_object()
        if not str(obj.username) == str(self.request.user):
            raise Http404

        return obj


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RepoList, self).get_context_data(**kwargs)
        context['user_data'] = UserModel.objects.get(pk=self.request.user.id)
        return context





