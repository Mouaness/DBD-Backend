# Generated by Django 5.0.3 on 2024-04-22 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activitylog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitylog',
            old_name='action_types',
            new_name='action_type',
        ),
    ]
