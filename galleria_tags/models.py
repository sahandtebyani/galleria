from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_tag_url(self):
        return f'/tags/{self.slug}'
