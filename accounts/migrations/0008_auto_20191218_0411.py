# Generated by Django 2.2.4 on 2019-12-18 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20191218_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequests',
            name='friend_since',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='following_since',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
