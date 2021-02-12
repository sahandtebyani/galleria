from django.urls import path
from .views import photo_detail, PhotoList, favorite

urlpatterns = [
    path('photos', PhotoList.as_view(), name='photo'),
    path('photos/<photo_id>/<title>', photo_detail, name='photo-detail'),
    path('favorite-post/<photo_id>', favorite, name='favorite-post')
]
