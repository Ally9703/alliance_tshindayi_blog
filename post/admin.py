from django.contrib import admin
from .models import *

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated","image")
    list_editable = ("published",)

admin.site.register(BlogPost, BlogPostAdmin)

    
admin.site.site_header = "DASHBOARD ALLIANCE TSHINDAYI"
