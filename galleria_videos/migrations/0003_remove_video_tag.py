# Generated by Django 3.1.1 on 2020-12-09 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleria_videos', '0002_video_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='tag',
        ),
    ]
