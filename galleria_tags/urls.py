from django.urls import path
from .views import TagList

urlpatterns = [
    path('tags/<tag_name>', TagList.as_view()),
]
