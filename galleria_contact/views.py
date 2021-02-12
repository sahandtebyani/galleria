from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs
from django.contrib import messages
from galleria_setting.models import Setting


def contact_form(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data.get('name')
        email = contact_form.cleaned_data.get('email')
        subject = contact_form.cleaned_data.get('subject')
        text = contact_form.cleaned_data.get('text')
        ContactUs.objects.create(name=name, email=email, subject=subject, text=text)
        contact_form = ContactForm()
        messages.success(request, 'Your message sent')

    setting = Setting.objects.first()
    context = {
        'contact_form': contact_form,
        'setting': setting
    }
    return render(request, 'contact/contact_form.html', context)
