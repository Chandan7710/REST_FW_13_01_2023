# Generated by Django 4.1.5 on 2023-01-10 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamplatform_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streamplatform',
            name='about',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='storyline',
            field=models.CharField(max_length=1000),
        ),
    ]
