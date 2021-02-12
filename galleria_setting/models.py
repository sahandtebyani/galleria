from django.db import models
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"logo/{final_name}"


class Setting(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    about_us = models.TextField()
    telephone = models.IntegerField()
    email = models.EmailField()
    logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    copyright = models.CharField(max_length=200)
    location = models.URLField()

    def __str__(self):
        return self.title