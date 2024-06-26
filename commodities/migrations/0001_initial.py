# Generated by Django 4.2.10 on 2024-04-25 21:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('location_coordinates_lat', models.CharField(max_length=255)),
                ('location_coordinates_long', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('commodity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commodities.commodity')),
                ('images', models.URLField(blank=True, max_length=2000, null=True)),
            ],
            bases=('commodities.commodity',),
        ),
        migrations.CreateModel(
            name='GuestHouse',
            fields=[
                ('commodity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='commodities.commodity')),
                ('category', models.CharField(max_length=100)),
                ('number_of_bathrooms', models.IntegerField(default=1)),
                ('number_of_bedrooms', models.IntegerField(default=1)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('accessibility', models.BooleanField(default=False)),
                ('food_type', models.CharField(choices=[('V', 'Vegan'), ('VE', 'Vegetarian'), ('M', 'Meat')], max_length=2)),
                ('images', models.URLField(blank=True, max_length=2000, null=True)),
            ],
            bases=('commodities.commodity',),
        ),
        migrations.AddField(
            model_name='commodity',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodities.district'),
        ),
    ]
