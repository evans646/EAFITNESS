# Generated by Django 4.0.3 on 2022-04-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0008_fitness'),
    ]

    operations = [
        migrations.AddField(
            model_name='beauty',
            name='text',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='culture',
            name='text',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='health',
            name='text',
            field=models.TextField(default=True),
        ),
        migrations.AddField(
            model_name='love',
            name='text',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='text',
            field=models.TextField(default=True),
        ),
    ]
