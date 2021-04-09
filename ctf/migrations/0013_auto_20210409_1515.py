# Generated by Django 3.1.7 on 2021-04-09 13:15

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0012_auto_20210409_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFFFF', max_length=18),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='validated',
            field=models.BooleanField(default=False),
        ),
    ]