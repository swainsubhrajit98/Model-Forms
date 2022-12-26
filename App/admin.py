from django.contrib import admin
from App.models import *
# Register your models here.

class WebpageCustomView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable = ['url']
    list_display_links = ['topic_name', 'name']
    list_per_page=5
    search_fields = ['name']
    list_filter = ['topic_name']
    

class AccessRecordsCustomView(admin.ModelAdmin):
    list_display=['name','date']
    
admin.site.register(Topic)
admin.site.register(Webpage,WebpageCustomView)
admin.site.register(AccessRecords,AccessRecordsCustomView)