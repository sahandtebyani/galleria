from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from galleria_photos.models import Photo
from galleria_videos.models import Video
from django.db.models import Q
from itertools import chain


# Create your views here.

class Search(ListView):
    template_name = 'serach/serach_page.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query)
        if query is not None:
            photos = Photo.objects.filter(lookup, active=True).distinct()
            videos = Video.objects.filter(lookup, active=True).distinct()
            return list(chain(photos, videos))
        else:
            return HttpResponse('nothing find')
