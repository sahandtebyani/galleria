"""galleria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from galleria import settings
from django.conf.urls.static import static
from .views import home_page, header, footer, about_us



urlpatterns = [
    path('', home_page, name='home-page'),
    path('', include('galleria_account.urls')),
    path('', include('galleria_photos.urls')),
    path('', include('galleria_videos.urls')),
    path('', include('galleria_search.urls')),
    path('', include('galleria_tags.urls')),
    path('', include('galleria_contact.urls')),
    path('about-us', about_us, name='about'),
    path('header', header, name='header'),
    path('footer', footer, name='footer'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
