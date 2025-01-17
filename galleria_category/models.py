from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()

    def __str__(self):
        return self.title