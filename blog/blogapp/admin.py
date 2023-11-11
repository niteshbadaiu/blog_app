from django.contrib import admin
from blogapp.models import Blog
# Register your models here.

# admin.site.register(Blog)

#step1 -> define admin class
class BlogAdmin(admin.ModelAdmin):
    list_display=["id","title","details","is_published","created_at"]
    list_filter=("cat","is_published")
#step2 ->: register model with ModelAdmin class
admin.site.register(Blog,BlogAdmin)
