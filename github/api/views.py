from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authentication import (
    BaseAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RepoSerializer, RepoStarSerializer, RepoUserModelSerializer, DeleteRepoSerializer
from github.models import RepoModel, RepoUserModel


class RepoCreateView(generics.CreateAPIView):
    serializer_class = RepoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # raise error if repository already exists for this user
        if RepoModel.objects.filter(
            repo_name=request.data["repo_name"], owner=request.user
        ).exists():
            return Response(
                {"message": "Repository already exists for this user"},
                status=400,
            )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "Repository created successfully", "data": serializer.data},
            status=201,
            headers=headers,
        )


class RepoListView(generics.ListAPIView):
    serializer_class = RepoSerializer
    queryset = RepoModel.objects.all()
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [IsAuthenticated]
    filter_fields = (
        "repo_language",
        "repo_stars",
        "repo_description",
    )


class RepoUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepoSerializer
    queryset = RepoModel.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Repository deleted successfully"},
            status=204
        )


class RepoDeleteView(generics.DestroyAPIView):
    serializer_class = DeleteRepoSerializer
    queryset = RepoModel.objects.all()
    permission_classes = [IsAuthenticated]


class RepoStarView(generics.UpdateAPIView):
    serializer_class = RepoStarSerializer
    queryset = RepoModel.objects.all()


class RepoUserModelCreate(generics.CreateAPIView):
    serializer_class = RepoUserModelSerializer

    def perform_create(self, serializer):
        serializer.validated_data["owner"] = self.request.user
        serializer.save()


class RepoUserListView(generics.ListAPIView):
    serializer_class = RepoUserModelSerializer
    queryset = RepoUserModel.objects.all()
