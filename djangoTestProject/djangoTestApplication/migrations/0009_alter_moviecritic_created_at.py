# Generated by Django 4.0.1 on 2022-01-31 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoTestApplication', '0008_moviecritic_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviecritic',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
