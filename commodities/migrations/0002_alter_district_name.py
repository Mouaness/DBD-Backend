# Generated by Django 4.2.10 on 2024-04-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
