# Generated by Django 4.2.10 on 2024-04-25 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('identifier', models.CharField(choices=[('C', 'CREATE'), ('R', 'READ'), ('U', 'UPDATE'), ('D', 'DELETE')], help_text='Type of CRUD operation', max_length=1)),
            ],
            options={
                'unique_together': {('name', 'identifier')},
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('permissions', models.ManyToManyField(related_name='types', to='users.permission')),
            ],
        ),
        migrations.CreateModel(
            name='InvitedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invited_at', models.DateTimeField(auto_now_add=True)),
                ('token', models.CharField(max_length=32, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invited_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BannedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banned_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(default='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='banned_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
