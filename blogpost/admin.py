from django.contrib import admin
from .models import BlogPost, contact, Comment, Reply

admin.site.register(BlogPost)
admin.site.register(contact)
admin.site.register(Comment)
admin.site.register(Reply)

