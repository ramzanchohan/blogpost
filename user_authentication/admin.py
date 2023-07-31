from django.contrib import admin
from .models import UserProfile
from django.utils.html import format_html


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "image_tag", 'image', "created_at"]

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:40px;height:20px;" />'.format(obj.image.url))
        return None
