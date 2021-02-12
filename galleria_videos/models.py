from django.contrib.auth.models import User
from django.db import models
import os
from galleria_category.models import Category

from galleria_tags.models import Tag


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_video_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"videos/{final_name}"


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"photos/{final_name}"


class VideoManager(models.Manager):
    def get_active_video(self):
        return self.get_queryset().filter(active=True)

    def get_video_tag(self, tag_name):
        return self.get_queryset().filter(tag__slug__iexact=tag_name)

    def get_video_id(self, video_id):
        q = self.get_queryset().filter(id=video_id)
        if q.count() == 1:
            return q.first()
        else:
            return None


class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    video = models.FileField(upload_to=upload_video_path, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    views = models.IntegerField(default=0)
    favorite = models.ManyToManyField(User, blank=True)

    objects = VideoManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/videos/{self.id}/{self.title}'
