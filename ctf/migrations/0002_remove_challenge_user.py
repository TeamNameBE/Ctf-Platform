# Generated by Django 3.1.7 on 2021-04-13 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0001_squashed_0014_auto_20210409_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='user',
        ),
    ]