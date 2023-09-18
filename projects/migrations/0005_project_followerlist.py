# Generated by Django 4.2.5 on 2023-09-17 12:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_alter_project_estimatedimplementationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='followerList',
            field=models.ManyToManyField(blank=True, related_name='followed_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]
