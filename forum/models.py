from django.db import models
from django_github import settings


class ForumThread(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    thread_video = models.FileField(upload_to='forum_videos')
    slug = models.CharField(max_length=200, editable=False, blank=True)

    def __str__(self):
        return str(self.owner) + '-' + str(self.title)


class ThreadComment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    thread = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)
    likes_count = models.IntegerField()

    def __str__(self):
        return str(self.owner) + str(self.comment_text)


