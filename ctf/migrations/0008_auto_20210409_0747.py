# Generated by Django 3.1.7 on 2021-04-09 07:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ctf', '0007_auto_20210409_0741'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Challenges',
            new_name='Challenge',
        ),
    ]
