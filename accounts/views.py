from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from . forms import UserModelForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


class RegisterForm(FormView):
    form_class = UserModelForm
    template_name = 'accounts/register.html'
    success_url = '/'


def accounts_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
      login(request, user)
      return HttpResponseRedirect(reverse('home'))

    else:
      return HttpResponseRedirect(reverse('accounts:login'))

  else:
    return render(request, 'accounts/login.html', {})





