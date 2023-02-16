# Generated by Django 4.1.4 on 2023-01-13 14:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_remove_userfollowing_following_by_userfollowing_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserFollowing',
        ),
    ]
