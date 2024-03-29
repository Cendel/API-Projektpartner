# Generated by Django 4.2.5 on 2023-09-26 21:49

from django.db import migrations, models
import project_attachments.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=project_attachments.models.upload_to_path)),
                ('file_name', models.CharField(blank=True, max_length=200, null=True)),
                ('file_extension', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
