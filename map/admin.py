from django.contrib import admin

# Register your models here.
from .models import Car

admin.site.site_header = 'Admin Dashboard'

class CarAdmin(admin.ModelAdmin):
    view_on_site = False
    change_list_template = 'admin/preview_template.html'

admin.site.register(Car, CarAdmin)
