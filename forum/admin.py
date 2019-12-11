from django.contrib import admin
from forum.models import ForumThread, ThreadComment


admin.site.register(ForumThread)
admin.site.register(ThreadComment)
