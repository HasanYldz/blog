from django.shortcuts import get_object_or_404, render, redirect
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


from .forms import NewPostForm, NewTopicForm, EditPostForm
from .models import Post, Topic, User


class index(View):
    def get(self, request):

        search_post = request.GET.get('search')
        if search_post:
            posts = Post.objects.filter(Q(title__icontains=search_post)
                                        | Q(author__username__icontains=search_post)
                                        | Q(topic__name__icontains=search_post)
                                        | Q(content__icontains=search_post))
        else:
            posts = Post.objects.filter(status=1, active=True).order_by('-pub_date')
        return render(request, 'blog/index.html', {'posts': posts})


class post_detail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, status=1, slug=slug, active=True)
        return render(request, 'blog/post_detail.html', {'post': post})


class topic_detail(View):
    def get(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        posts = Post.objects.filter(status=1, topic=topic, active=True).order_by('-pub_date')
        return render(request, 'blog/topic_detail.html', {'posts': posts, 'topic':topic})


class author_detail(View):
    def get(self, request, id):
        author = get_object_or_404(User, id=id)
        if request.user != author:
            posts = Post.objects.filter(status=1, author=author, active=True).order_by('-pub_date')
        else:
            posts = Post.objects.filter(author=author).order_by('-pub_date')
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
            post.author = request.user
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


class edit_post(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = EditPostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        old_status = post.status
        form = EditPostForm(request.POST, instance=post)

        if form.is_valid():

            if old_status == 0:
                if post.status == 1:
                    post.pub_date = timezone.now()

            post.save()

            if post.active:
                return redirect('blog:post_detail', post.slug)

            return redirect('blog:index')
