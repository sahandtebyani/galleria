from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from galleria_videos.models import Video


class VideoList(ListView):
    template_name = 'videos/video_list.html'
    paginate_by = 6

    def get_queryset(self):
        video = Video.objects.get_active_video()
        return video


def video_detail(request, *args, **kwargs):
    selected_video = kwargs['video_id']
    video = Video.objects.get_video_id(selected_video)
    if video is None:
        raise Http404('video not found')

    tag = video.tag.all()

    video.views += 1
    video.save()

    is_favorite = False
    if video.favorite.filter(id=request.user.id).exists():
        is_favorite = True

    context = {
        'video': video,
        'tags': tag,
        'is_favorite': is_favorite,
    }
    return render(request, 'videos/video_detail.html', context)


def favorite_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if video.favorite.filter(id=request.user.id).exists():
        video.favorite.remove(request.user)
    else:
        video.favorite.add(request.user)
    return HttpResponseRedirect(video.get_absolute_url())
