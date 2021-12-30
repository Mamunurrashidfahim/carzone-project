from django.contrib import admin
from pages.models import Teams
from django.utils.html import format_html


class TeamsAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60" />'.format(object.photo.url))
    
    thumbnail.short_description ='Photo'
    
    list_display =('id','thumbnail','first_name','last_name','designation','create_at')
    list_display_links =('id','thumbnail','first_name')
    search_fields =('first_name','last_name','designation')
    list_filter = ('designation',)
    
admin.site.register(Teams,TeamsAdmin)

