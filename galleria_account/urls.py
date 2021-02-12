from django.urls import path
from .views import log_in, register_form, log_out, user_profile, edit_user_info, LikedPhoto, PasswordChange, LikedVideos

urlpatterns = [
    path('login', log_in, name='login'),
    path('register', register_form, name='register'),
    path('logout', log_out, name='logout'),
    path('profile', user_profile, name='profile'),
    path('profile/edit', edit_user_info, name='edit_info'),
    path('profile/liked-photos', LikedPhoto.as_view(), name='liked-photos'),
    path('profile/liked-videos', LikedVideos.as_view(), name='liked-videos'),
    path('profile/change-password', PasswordChange.as_view(template_name='account/change_password.html'),
         name='change-password'),

]
