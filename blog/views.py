from django.contrib.auth.models import User
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

class topic_detail(View):
    def get(self, request, slug):
        topic = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/post_detail.html')

class add_post(View):
    def get(self, request):
        return render(request, 'blog/add_post.html')
    def post(self, request):
        title = request.POST['title']
        content = request.POST['content']

        user = User.objects.first()

        pass