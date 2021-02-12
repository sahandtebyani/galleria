from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from .forms import LogInForm, RegisterForm, EditUserForm, ChangePassword
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from galleria_photos.models import Photo
from galleria_videos.models import Video
from django.urls import reverse_lazy


def log_in(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        login_form = LogInForm(request.POST or None)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
            else:
                raise login_form.add_error('email', 'something went wrong')
    else:
        login_form = LogInForm()

    context = {
        'log_in': login_form
    }
    return render(request, 'account/login_page.html', context)


def register_form(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method == 'POST':
        register = RegisterForm(request.POST or None)
        if register.is_valid():
            first_name = register.cleaned_data.get('first_name')
            last_name = register.cleaned_data.get('last_name')
            email = register.cleaned_data.get('email')
            password = register.cleaned_data.get('password')
            User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                     password=password)
            return redirect('/login')
    else:
        register = RegisterForm()

    context = {
        'register': register
    }
    return render(request, 'account/register_page.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    context = {
        'info': user
    }
    return render(request, 'account/user_profile.html', context)


@login_required(login_url='/login')
def sidebar(request):
    context = {}
    return render(request, 'account/panel_sidebar.html', context)


@login_required(login_url='/login')
def edit_user_info(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    if user is None:
        raise Http404('user not found')
    edit_form = EditUserForm(request.POST or None, initial={'first_name': user.first_name, 'last_name': user.last_name})
    if edit_form.is_valid():
        first_name = edit_form.cleaned_data.get('first_name')
        last_name = edit_form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()

    context = {
        'edite_form': edit_form
    }
    return render(request, 'account/edit_profile.html', context)


class LikedPhoto(LoginRequiredMixin, ListView):
    template_name = 'account/liked_photos.html'
    paginate_by = 6
    login_url = '/login'

    def get_queryset(self):
        user = self.request.user.id
        return Photo.objects.filter(favorite=user)



class LikedVideos(LoginRequiredMixin, ListView):
    template_name = 'account/liked_videos.html'
    paginate_by = 12
    login_url = '/login'

    def get_queryset(self):
        user = User.objects.filter(id=self.request.user.id).first()
        return Video.objects.filter(favorite=user)


class PasswordChange(PasswordChangeView):
    form_class = ChangePassword
    success_url = reverse_lazy('profile')
