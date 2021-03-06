# Generated by Django 2.2.4 on 2019-12-07 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('github', '0004_remove_repousermodel_user_repo_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepoTopicModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200)),
                ('topic_score', models.IntegerField()),
                ('topic_description', models.CharField(default=None, max_length=500)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repo_topic_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
