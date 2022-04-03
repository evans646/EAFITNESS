# Generated by Django 4.0.3 on 2022-04-03 10:06

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0006_auto_20220328_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beauty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('premium', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('premium', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('text', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('date', models.DateTimeField()),
                ('premium', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('premium', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Love',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('premium', models.BooleanField(default=True)),
            ],
        ),
    ]
