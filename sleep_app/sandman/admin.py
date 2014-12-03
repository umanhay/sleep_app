from django.contrib import admin
from sandman.models import Mode, Contacts

admin.site.register(Mode)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'charmed')

admin.site.register(Contacts, ContactsAdmin)
