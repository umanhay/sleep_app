from django.contrib import admin
from sandman.models import Mode, Contacts, Help

admin.site.register(Mode)

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'charmed')

class HelpAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')

admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Help, HelpAdmin)