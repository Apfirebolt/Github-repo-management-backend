from django.db import models
from django_github.settings import AUTH_USER_MODEL


class RepoModel(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, related_name='repo_owner', on_delete=models.CASCADE)
    repo_creator = models.CharField(max_length=100)
    repo_language = models.CharField(max_length=50)
    repo_name = models.CharField(max_length=200)
    repo_description = models.CharField(max_length=500)
    repo_url = models.URLField()
    repo_stars = models.IntegerField()
    repo_score = models.IntegerField()
    repo_watchers = models.IntegerField()
    repo_created_on = models.DateTimeField()
    repo_forked = models.IntegerField(default=0)
    is_favorited = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner) + ' - ' + str(self.repo_name)


class RepoUserModel(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, related_name='repo_user_owner', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    user_url = models.URLField()
    user_image_url = models.URLField()

    def __str__(self):
        return str(self.owner) + ' - ' + str(self.user_name)

