# Generated by Django 4.2.5 on 2023-09-19 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_messages', '0003_rename_createddate_message_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='sender',
        ),
    ]
