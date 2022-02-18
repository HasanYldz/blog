from django import forms
from .models import Post, Topic


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'author', 'topic']


class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']

    class LoginForm(forms.Form):
        email = forms.CharField(max_length=64)
        password = forms.CharField(widget=forms.PasswordInput(render_value=False), max_length=30)