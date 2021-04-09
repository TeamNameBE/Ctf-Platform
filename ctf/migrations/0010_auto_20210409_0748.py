# Generated by Django 3.1.7 on 2021-04-09 07:48

import ctf.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctf', '0009_auto_20210409_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(ctf.models.get_sentinel_user), to=settings.AUTH_USER_MODEL),
        ),
    ]
