from django.shortcuts import render
from galleria_setting.models import Setting
from galleria_photos.models import Photo


def header(request):
    context = {}
    return render(request, 'shared/Header.html', context)


def footer(request):
    context = {}
    return render(request, 'shared/Footer.html', context)


def about_us(request):
    setting = Setting.objects.first()
    context = {
        'setting': setting
    }
    return render(request, 'about_us.html', context)


def home_page(request):
    latest_photo = Photo.objects.order_by('-date').all()[:4]
    context = {
        'latest': latest_photo
    }
    return render(request, 'home_page.html', context)
