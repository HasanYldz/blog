from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from django.http import HttpResponse

from .models import Post

class index(View):
    def get(self, request):
        posts = Post.objects.filter(status=1)
        return render(request, 'blog/index.html', {'posts':posts})

class post_detail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/post_detail.html', {'post':post})