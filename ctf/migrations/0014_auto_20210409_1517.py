# Generated by Django 3.1.7 on 2021-04-09 13:17

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0013_auto_20210409_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]