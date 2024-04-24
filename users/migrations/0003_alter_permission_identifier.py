# Generated by Django 4.2.10 on 2024-04-20 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='identifier',
            field=models.CharField(choices=[('C', 'CREATE'), ('R', 'READ'), ('U', 'UPDATE'), ('D', 'DELETE')], help_text='Type of CRUD operation', max_length=1),
        ),
    ]