from django.http import Http404, HttpResponseRedirect , HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, UpdateView
from galleria_photos.models import Photo
from galleria_tags.models import Tag


class PhotoList(ListView):
    template_name = 'photos/photo_list.html'
    paginate_by = 30

    def get_queryset(self):
        return Photo.objects.get_active_photos()


def photo_detail(request, *args, **kwargs):
    selected_photo = kwargs['photo_id']
    photo = Photo.objects.get_photo_by_id(selected_photo)

    if photo is None or not photo.active:
        raise Http404('photo is not available')

    tag = photo.tag.all()

    photo.views += 1
    photo.save()

    is_favorite = False
    if photo.favorite.filter(id=request.user.id).exists():
        is_favorite = True

    context = {
        'photo': photo,
        'tags': tag,
        'is_favorite': is_favorite
    }
    return render(request, 'photos/photo_detail.html', context)


def favorite(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    if photo.favorite.filter(id=request.user.id).exists():
        photo.favorite.remove(request.user)
    else:
        photo.favorite.add(request.user)
    return HttpResponseRedirect(photo.get_absolute_url())
