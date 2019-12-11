from django import forms
from forum.models import ForumThread, ThreadComment


class ThreadForm(forms.ModelForm):

    class Meta:
        model = ForumThread
        fields = ('title', 'content', 'thread_video',)



