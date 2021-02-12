from django.contrib import admin

from galleria_contact.models import ContactUs


class ContactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_read', 'date']
    list_filter = ['is_read']


admin.site.register(ContactUs, ContactAdmin)
