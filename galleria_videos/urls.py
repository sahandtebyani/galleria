from django.urls import path
from .views import video_detail, VideoList, favorite_video

urlpatterns = [
    path('videos', VideoList.as_view(), name='video'),
    path('videos/<video_id>/<title>', video_detail, name='video-detail'),
    path('favorite-video/<video_id>', favorite_video, name='favorite-video'),
]
