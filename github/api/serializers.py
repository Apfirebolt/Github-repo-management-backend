from rest_framework import serializers
from github.models import RepoModel
from rest_framework.validators import UniqueValidator


class RepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = RepoModel
        fields = ('owner','repo_creator', 'repo_language', 'repo_name', 'repo_forked', 'repo_stars', 'repo_score',
              'repo_description', 'repo_url', 'repo_watchers', 'repo_created_on')
        extra_kwargs = {
          'owner': {'read_only': True},
        }



    # def create(self, validated_data):
    #     pass
