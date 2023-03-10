# Generated by Django 4.1.4 on 2023-01-13 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_alter_customuser_biography_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfollowing',
            name='user',
        ),
        migrations.AddField(
            model_name='userfollowing',
            name='following_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userfollowing',
            name='following',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
