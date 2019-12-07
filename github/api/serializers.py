from rest_framework import serializers
from github.models import RepoModel
from rest_framework.validators import UniqueValidator


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepoModel
        fields = ('id', 'owner','repo_creator', 'repo_language', 'repo_name', 'repo_forked', 'repo_stars', 'repo_score',
              'repo_description', 'repo_url', 'repo_watchers', 'repo_created_on', 'is_favorited',)
        extra_kwargs = {
          'owner': {'read_only': True},
          'id': {'read_only': True},
          'is_favorited': {'read_only': True}
        }


class RepoStarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepoModel
        fields = ('is_favorited',)

