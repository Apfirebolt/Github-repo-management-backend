# Generated by Django 2.2.4 on 2019-12-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_threadcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumthread',
            name='slug',
            field=models.CharField(blank=True, editable=False, max_length=200),
        ),
    ]