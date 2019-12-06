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


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            print('valid data')
        else:
            print('Invalid data passed..')

        print('The data is : ', serializer.validated_data)
        serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
        serializer.save()


class ListUserView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    filter_backends = (DjangoFilterBackend, )
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_fields = ('username', 'about_me', 'first_name',)


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