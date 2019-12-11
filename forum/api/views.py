from rest_framework import generics
from django.dispatch import receiver
from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializers import ThreadSerializer, ThreadCommentSerializer
from forum.models import ForumThread, ThreadComment


class ThreadCreateView(generics.CreateAPIView):
    serializer_class = ThreadSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user;
        serializer.save()


class ThreadListView(generics.ListAPIView):
    serializer_class = ThreadSerializer
    queryset = ForumThread.objects.all()
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class ThreadCommentCreateView(generics.CreateAPIView):
    serializer_class = ThreadCommentSerializer

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user;
        serializer.save()


class ThreadCommentListView(generics.ListAPIView):
    serializer_class = ThreadCommentSerializer
    queryset = ThreadComment.objects.all()
    # permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]