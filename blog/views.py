from django.shortcuts import get_object_or_404, render, redirect
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import NewPostForm, NewTopicForm
from .models import Post, Topic, User


class index(View):
    def get(self, request):
        posts = Post.objects.filter(status=1)
        return render(request, 'blog/index.html', {'posts': posts})


class post_detail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/post_detail.html', {'post': post})


class topic_detail(View):
    def get(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        posts = Post.objects.filter(status=1, topic=topic)
        return render(request, 'blog/topic_detail.html', {'posts': posts, 'topic':topic})


class author_detail(View):
    def get(self, request, id):
        author = get_object_or_404(User, id=id)
        posts = Post.objects.filter(status=1, author=author)
        return render(request, 'blog/author_detail.html', {'posts': posts, 'author':author})



class add_post(LoginRequiredMixin, View):
    def get(self, request):
        form = NewPostForm()
        return render(request, 'blog/add_post.html', {'form': form})

    def post(self, request):
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            if post.status == 1:
                post.pub_date = timezone.now()

            post.slug = slugify(post.title)
            post.save()

            return redirect('blog:post_detail', post.slug)



class add_topic(LoginRequiredMixin, View):
    def get(self, request):
        form = NewTopicForm()
        return render(request, 'blog/add_topic.html', {'form': form})

    def post(self, request):
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)

            topic.slug = slugify(topic.name)
            topic.save()

            return redirect('blog:topic_detail', topic.slug)
