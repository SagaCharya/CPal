import helpers
from django.contrib import admin
from .models import Course, Lesson
from django.utils.html import format_html
from cloudinary import CloudinaryImage


class LessonInline(admin.StackedInline):
    model = Lesson
    readonly_fields = ["updated", "public_id", "display_image"]
    extra = 0

    def display_image(self, obj, *args, **kwargs):
        url = helpers.get_cloudinary_imgage_object(
            obj, 
            width=200, 
            field_name="thumbnail"
        )
        return format_html(f"<img src={url} />")

    display_image.short_description = "Current Image"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ["title", "access", "status"]
    list_filter = ["access", "status"]
    fields = [
        "public_id",
        "title",
        "description",
        "image",
        "access",
        "status",
        "display_image",
    ]
    readonly_fields = ["public_id", "display_image"]

    def display_image(self, obj, *args, **kwargs):
        url = helpers.get_cloudinary_imgage_object(
            obj, 
            width=200, 
            field_name="image"
        )
        return format_html(f"<img src={url} />")

    display_image.short_description = "Current Image"
