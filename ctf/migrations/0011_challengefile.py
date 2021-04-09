# Generated by Django 3.1.7 on 2021-04-09 11:58

import ctf.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctf', '0010_auto_20210409_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChallengeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=ctf.utils.chall_file_upload)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.challenge')),
            ],
        ),
    ]