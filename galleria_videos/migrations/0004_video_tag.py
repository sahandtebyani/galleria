# Generated by Django 3.1.1 on 2020-12-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleria_tags', '0002_auto_20201207_2049'),
        ('galleria_videos', '0003_remove_video_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='tag',
            field=models.ManyToManyField(blank=True, to='galleria_tags.Tag'),
        ),
    ]
