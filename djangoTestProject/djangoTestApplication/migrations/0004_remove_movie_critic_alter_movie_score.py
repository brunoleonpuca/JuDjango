# Generated by Django 4.0.1 on 2022-01-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTestApplication', '0003_movie_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='critic',
        ),
        migrations.AlterField(
            model_name='movie',
            name='score',
            field=models.IntegerField(),
        ),
    ]