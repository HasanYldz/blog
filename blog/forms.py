from django.core.exceptions import ValidationError
from django.contrib import admin

from django import forms
from .models import Post, Topic, AboutPage


class NewPostForm(forms.ModelForm):
    topic = forms.ModelChoiceField(queryset=Topic.objects.all(), required=True, widget=forms.Select())

    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'topic', 'related_posts', 'post_picture']

    def clean(self):
        related_posts = self.cleaned_data.get('related_posts')
        if related_posts.count() > 3:
            raise ValidationError('To many related posts!')
        return self.cleaned_data


class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=30)


class EditPostForm(NewPostForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'topic', 'active', 'related_posts', 'post_picture']


class NewPostAdminForm(NewPostForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = NewPostAdminForm


class EditAboutPageForm(forms.ModelForm):
    class Meta:
        model = AboutPage
        fields = ['content']
