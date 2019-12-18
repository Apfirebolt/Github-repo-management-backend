from rest_framework import generics
from . serializers import UserSerializer
from accounts.models import UserModel
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.http import HttpResponseForbidden
from . permission import IsUserAuthenticated
from rest_framework.exceptions import PermissionDenied


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsUserAuthenticated]
    authentication_classes = [SessionAuthentication]
    filter_fields = ('username', 'about_me', 'first_name',)

    def get_queryset(self):
        queryset = UserModel.objects.all()
        search_user = self.request.query_params.get('username')
        search_email = self.request.query_params.get('email')

        if search_user:
            queryset = queryset.filter(username__icontains=search_user)
        elif search_email:
            queryset = queryset.filter(email__icontains=search_email)
        elif search_user and search_email:
            queryset = queryset.filter(Q(username__icontains=search_user) & Q(email__icontains=search_email))

        return queryset


class UpdateUserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def perform_update(self, serializer):
        serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
        serializer.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)