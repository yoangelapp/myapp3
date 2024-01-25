from django.contrib import admin
from .models import producto

# Register your models here.

class producto_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(producto, producto_admin)
