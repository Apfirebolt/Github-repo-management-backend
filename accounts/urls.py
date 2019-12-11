from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.RepoList.as_view(), name='dashboard'),
    path('api/', include(('accounts.api.urls', 'accounts.api'), namespace='accounts-api')),
    path('register/', views.RegisterForm.as_view(), name='register'),
    path('settings/<int:pk>', views.EditAccountSettings.as_view(), name='settings'),
    path('login/', views.accounts_login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
