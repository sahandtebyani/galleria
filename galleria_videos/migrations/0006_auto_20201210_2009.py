# Generated by Django 3.1.1 on 2020-12-10 16:39

from django.db import migrations, models
import galleria_videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('galleria_videos', '0005_auto_20201210_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=galleria_videos.models.upload_image_path),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=galleria_videos.models.upload_video_path),
        ),
    ]
