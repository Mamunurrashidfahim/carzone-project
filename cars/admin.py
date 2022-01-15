from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60" />'.format(object.car_photo.url))
    
    thumbnail.short_description ='Car Images'

    list_display=('id','thumbnail','car_title','city','color','model','year','body_style','fuel_type','is_featured')
    list_display_links =('id','thumbnail','car_title')
    list_editable =('is_featured',)
    search_fields =('id','car_title','city','color','model','year','body_style')
    list_filter =('city','color','model','year','body_style')
admin.site.register(Car,CarAdmin)
