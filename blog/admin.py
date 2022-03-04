from django.contrib import admin

from .models import Post, Topic, Subscriber, AboutPage
from .forms import PostAdmin

admin.site.register(Post, PostAdmin)
admin.site.register(Topic)
admin.site.register(Subscriber)
admin.site.register(AboutPage)
