from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

from .forms import NewPostForm, NewTopicForm, EditPostForm, EditAboutPageForm
from .models import Post, Topic, User, Subscriber, PUBLISHED, DRAFT, AboutPage

from hitcount.views import HitCountMixin
from hitcount.models import HitCount


class IndexView(View):
    def get(self, request):
        search_post = request.GET.get('search')
        if search_post:
            posts = Post.objects.filter(Q(title__icontains=search_post)
                                        | Q(author__username__icontains=search_post)
                                        | Q(topic__name__icontains=search_post)
                                        | Q(content__icontains=search_post))
        else:
            sort_method = request.GET.get('sort')

            if sort_method:
                posts = Post.objects.filter(status=PUBLISHED, active=True).order_by(sort_method)
            else:
                posts = Post.objects.filter(status=PUBLISHED, active=True).order_by('-pub_date')

        return render(request, 'blog/index.html', {'posts': posts})


class PostDetailView(View, HitCountMixin):
    def get(self, request, slug):
        post = get_object_or_404(Post, status=PUBLISHED, slug=slug, active=True)

        hit_count = HitCount.objects.get_for_object(post)
        hit_count_response = HitCountMixin.hit_count(request, hit_count)

        token = request.secretballot_token
        voted = 0
        try:
            voted = post.votes.get(token=token).vote
        except ObjectDoesNotExist:
            pass

        return render(request, 'blog/post_detail.html', {'post': post, 'voted': voted})

    def post(self, request, slug):
        post = get_object_or_404(Post, status=PUBLISHED, slug=slug, active=True)
        vote = request.POST.get('like')
        token = request.secretballot_token
        post.remove_vote(token)
        post.add_vote(token, vote)

        response = HttpResponse()
        return response


class TopicDetailView(View):
    def get(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        posts = Post.objects.filter(status=PUBLISHED, topic=topic, active=True).order_by('-pub_date')
        return render(request, 'blog/topic_detail.html', {'posts': posts, 'topic': topic})


class AuthorDetailView(View):
    def get(self, request, id):
        author = get_object_or_404(User, id=id)
        if request.user != author:
            posts = Post.objects.filter(status=PUBLISHED, author=author, active=True).order_by('-pub_date')
        else:
            posts = Post.objects.filter(author=author).order_by('-pub_date')
        return render(request, 'blog/author_detail.html', {'posts': posts, 'author': author})


class AddPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = NewPostForm()
        return render(request, 'blog/add_post.html', {'form': form})

    def post(self, request):
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)

            if post.status == PUBLISHED:
                post.pub_date = timezone.now()

            post.slug = slugify(post.title)
            post.author = request.user

            post.save()

            for selected_post in form.cleaned_data['related_posts']:
                post.related_posts.add(selected_post)

            if post.related_posts.count() < 3:
                rel_posts = Post.objects.filter(status=PUBLISHED, active=True, topic=post.topic).exclude(id=post.id).order_by(
                    '-pub_date')

                for e in rel_posts:
                    if not post.related_posts.contains(e):
                        post.related_posts.add(e)
                        if post.related_posts.count() > 2:
                            break

            if post.related_posts.count() < 3:
                rel_posts = Post.objects.filter(status=PUBLISHED, active=True).exclude(id=post.id, topic=post.topic).order_by(
                    '-pub_date')

                for e in rel_posts:
                    if not post.related_posts.contains(e):
                        post.related_posts.add(e)
                        if post.related_posts.count() > 2:
                            break

            post.save()

            if post.status == PUBLISHED:
                return redirect('blog:post_detail', post.slug)
            else:
                return redirect('blog:index')
        else:
            return redirect('blog:index')


class AddTopicView(LoginRequiredMixin, View):
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


class EditPostView(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = EditPostForm(instance=post)
        return render(request, 'blog/edit_post.html', {'form': form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        old_status = post.status
        form = EditPostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            if old_status == DRAFT:
                if post.status == PUBLISHED:
                    post.pub_date = timezone.now()

            post.save()

            for selected_post in form.cleaned_data['related_posts']:
                post.related_posts.add(selected_post)

            if post.related_posts.count() < 3:
                rel_posts = Post.objects.filter(status=PUBLISHED, active=True, topic=post.topic).order_by('-pub_date')
                posts_needed = 3 - post.related_posts.count()

                if posts_needed + 1 > rel_posts.count():
                    posts_needed = rel_posts.count() - 1

                for i in range(1, posts_needed + 1):
                    post.related_posts.add(rel_posts[i])

            post.save()

            if post.active and post.status == PUBLISHED:
                return redirect('blog:post_detail', post.slug)
            else:
                return redirect('blog:index')

        return redirect('blog:index')


class SubscriptionView(View):
    def post(self, request):
        new_subscriber = Subscriber()
        new_subscriber.email = request.POST['mail']

        try:
            Subscriber.objects.get(email=new_subscriber.email)
        except ObjectDoesNotExist:
            new_subscriber.save()

        return redirect('blog:index')


class AllTopicsView(View):
    def get(self, request):
        topics = Topic.objects.all()
        return render(request, 'blog/all_topics.html', {'topics': topics})


class AboutView(View):
    def get(self, request):
        about = get_object_or_404(AboutPage, pk=1)
        form = EditAboutPageForm(instance=about)
        return render(request, 'blog/about.html', {'about': about.content, 'form': form})

    def post(self, request):
        about = get_object_or_404(AboutPage, pk=1)
        form = EditAboutPageForm(request.POST, instance=about)

        if form.is_valid():
            about = form.save(commit=False)
            about.save()

        return redirect('blog:about')
