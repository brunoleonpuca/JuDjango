# Generated by Django 4.0.1 on 2022-01-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTestApplication', '0004_remove_movie_critic_alter_movie_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='critic',
            field=models.TextField(default=1, max_length=1024),
            preserve_default=False,
        ),
    ]
