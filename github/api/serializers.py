from rest_framework import serializers
from github.models import RepoModel, RepoUserModel, RepoTopicModel
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


class RepoUserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepoUserModel
        fields = ('owner','user_name', 'user_url', 'user_image_url',)
        extra_kwargs = {
          'owner': {'read_only': True},
        }


class RepoTopicModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepoTopicModel
        fields = ('owner', 'topic_name', 'topic_score', 'topic_description',)
        extra_kwargs = {
          'owner': {'read_only': True},
        }


class RepoTopicDescriptionEdit(serializers.ModelSerializer):

    class Meta:
        model = RepoTopicModel
        fields = ('topic_description',)
