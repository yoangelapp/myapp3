from django.contrib import admin
from .models import contactanos

# Register your models here.

class contactanos_admin(admin.ModelAdmin):
    readonly_fields=('created',)
    

admin.site.register(contactanos, contactanos_admin)


