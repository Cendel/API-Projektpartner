# Generated by Django 4.2.5 on 2023-09-18 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_messages', '0002_message_createddate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='createdDate',
            new_name='created_date',
        ),
    ]
