# Generated by Django 4.2.5 on 2023-09-20 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_participantlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='maxSharesPerPerson',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='participantCount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='sharesTaken',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='totalShares',
            field=models.PositiveIntegerField(default=0),
        ),
    ]