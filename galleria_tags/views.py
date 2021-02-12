from django.http import Http404
from django.shortcuts import render
from .models import Tag
from galleria_videos.models import Video
from galleria_photos.models import Photo
from django.views.generic import ListView
from itertools import chain


class TagList(ListView):
    template_name = 'tags/tag_list.html'
    paginate_by = 6

    def get_queryset(self, *args, **kwargs):
        tag_name = self.kwargs['tag_name']
        tag = Tag.objects.filter(slug__iexact=tag_name).first()
        if tag is None:
            raise Http404('tag not found')
        photo = Photo.objects.get_photos_by_tag(tag_name)
        video = Video.objects.get_video_tag(tag_name)
        return list(chain(photo, video))
