# Generated by Django 3.1.7 on 2021-04-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0006_auto_20210409_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(default='bg-green-300', max_length=32),
        ),
    ]
