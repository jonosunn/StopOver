from django.contrib import admin

# Register your models here.
from .models import Car

admin.site.site_header = 'Admin Dashboard'

class CarAdmin(admin.ModelAdmin):
    view_on_site = False
    change_form_template = 'admin/map/change_form.html'

admin.site.register(Car, CarAdmin)
