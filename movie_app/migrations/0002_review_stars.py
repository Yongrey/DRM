# Generated by Django 4.1.1 on 2022-09-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.SmallIntegerField(default=0),
        ),
    ]
