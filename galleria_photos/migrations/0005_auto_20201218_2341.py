# Generated by Django 3.1.1 on 2020-12-18 20:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galleria_photos', '0004_photo_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='favorite',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
