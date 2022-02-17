from django import forms
from .models import Topic


class NewTopicForm(forms.ModelForm):
    content = forms

    class Meta:
        model = Topic
        fields = ['title', 'content']