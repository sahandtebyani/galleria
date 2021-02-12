from django.urls import path

from galleria_contact.views import contact_form

urlpatterns = [
    path('contact', contact_form, name='contact')
]
