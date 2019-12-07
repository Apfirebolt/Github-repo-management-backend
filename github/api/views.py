from rest_framework import generics
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from . serializers import RepoSerializer, RepoStarSerializer
from github.models import RepoModel


class RepoCreateView(generics.CreateAPIView):
    serializer_class = RepoSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user;
        serializer.save()


class RepoListView(generics.ListAPIView):
    serializer_class = RepoSerializer
    queryset = RepoModel.objects.all()
    filter_backends = (DjangoFilterBackend, )
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    filter_fields = ('repo_language', 'repo_stars', 'repo_description',)


class RepoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepoSerializer
    queryset = RepoModel.objects.all()


class RepoDeleteView(generics.DestroyAPIView):
    serializer_class = RepoSerializer
    queryset = RepoModel.objects.all()


class RepoStarView(generics.UpdateAPIView):
    serializer_class = RepoStarSerializer
    queryset = RepoModel.objects.all()



