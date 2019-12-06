from django.urls import path, include
from rest_framework.authtoken import views as auth_token_view
from . import views

urlpatterns = [
    path('api-token-auth', auth_token_view.obtain_auth_token),
    path('list', views.ListUserView.as_view(), name='user-list'),
    path('create', views.CreateUserView.as_view(), name='user-create'),
    path('update/<int:pk>', views.UpdateUserView.as_view(), name='user-update'),
]