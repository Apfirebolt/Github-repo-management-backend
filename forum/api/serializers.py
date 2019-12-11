from rest_framework import serializers
from forum.models import ForumThread, ThreadComment


class ThreadSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForumThread
        fields = ('owner', 'id', 'title', 'content', 'thread_video',)
        extra_kwargs = {
          'owner': {'read_only': True},
          'id': {'read_only': True},
        }


class ThreadCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadComment
        fields = ('owner', 'id', 'thread', 'comment_text', 'likes_count',)
        extra_kwargs = {
          'owner': {'read_only': True},
          'id': {'read_only': True},
        }