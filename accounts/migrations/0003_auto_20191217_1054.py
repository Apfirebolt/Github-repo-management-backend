# Generated by Django 2.2.4 on 2019-12-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191211_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='profile_image',
            field=models.ImageField(blank=True, default='1.png', upload_to='profile_pics'),
        ),
    ]