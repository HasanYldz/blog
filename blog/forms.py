from django.core.exceptions import ValidationError
from django.contrib import admin

from django import forms
from .models import Post, Topic


class NewPostForm(forms.ModelForm):
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


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'topic', 'active', 'related_posts']

    def clean(self):
        related_posts = self.cleaned_data.get('related_posts')
        if related_posts.count() > 3:
            raise ValidationError(_("Too many related posts!"))
        return self.cleaned_data


class NewPostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean(self):
        related_posts = self.cleaned_data.get('related_posts')
        if related_posts.count() > 3:
            raise ValidationError(_('Too many related posts!'))
        return self.cleaned_data


class PostAdmin(admin.ModelAdmin):
    form = NewPostAdminForm
