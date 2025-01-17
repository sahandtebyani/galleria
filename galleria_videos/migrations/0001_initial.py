# Generated by Django 3.1.1 on 2020-12-03 17:05

from django.db import migrations, models
import galleria_videos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('galleria_tags', '0001_initial'),
        ('galleria_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to=galleria_videos.models.upload_image_path)),
                ('active', models.BooleanField(default=True)),
                ('views', models.IntegerField(default=0)),
                ('category', models.ManyToManyField(blank=True, to='galleria_category.Category')),
                ('tag', models.ManyToManyField(blank=True, to='galleria_tags.Tag')),
            ],
        ),
    ]
