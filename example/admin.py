from django.contrib import admin

# Register your models here.

from example.models.post import Post

admin.site.register(Post)