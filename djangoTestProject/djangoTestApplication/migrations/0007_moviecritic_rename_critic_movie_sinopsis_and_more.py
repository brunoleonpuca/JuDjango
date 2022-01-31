# Generated by Django 4.0.1 on 2022-01-31 14:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTestApplication', '0006_alter_movie_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieCritic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('critic', models.TextField(max_length=1000000)),
                ('score', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='critic',
            new_name='sinopsis',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='score',
        ),
    ]
