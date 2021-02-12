from django.db import models
import os
from galleria_category.models import Category
from galleria_tags.models import Tag
from django.contrib.auth.models import User


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.title}{ext}"
    return f"photos/{final_name}"


class PhotoManager(models.Manager):
    def get_active_photos(self):
        return self.get_queryset().filter(active=True)

    def get_photos_by_category(self, category_name):
        return self.get_queryset().filter(category__slug__iexact=category_name, active=True)

    def get_photos_by_tag(self, tag_name):
        return self.get_queryset().filter(tag__slug__iexact=tag_name, active=True)

    def get_photo_by_id(self, photo_id):
        qs = self.get_queryset().filter(id=photo_id)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def get_favorite_photos(self, user):
        return self.get_queryset().filter(favorite=self.request.user, active=True)


class Photo(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(unique=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)
    tag = models.ManyToManyField(Tag, blank=True)
    views = models.IntegerField(default=0)
    favorite = models.ManyToManyField(User, blank=False)

    objects = PhotoManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/photos/{self.id}/{self.title.replace(' ', '-')}"

