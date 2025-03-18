from django.contrib import admin
from .models import Course
from django.utils.html import format_html
from cloudinary import CloudinaryImage

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'access', 'status']
    list_filter = ['access', 'status']
    fields = ['title', 'description', 'image', 'access', 'status', 'display_image']
    readonly_fields = ['display_image']
    
    def display_image(self,obj, *args, **kwargs):
        url = obj.image.url
        cloudinary_id = str(obj.image)
        cloudinary_html =CloudinaryImage(cloudinary_id).image(width=500)
        return format_html(cloudinary_html)

    display_image.short_description = 'Current Image'
        


# admin.site.register(Course)