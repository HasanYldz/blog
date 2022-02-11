from django.contrib import admin

from .models import Post, Topic, Author

admin.site.register(Post)
admin.site.register(Topic)
admin.site.register(Author)
