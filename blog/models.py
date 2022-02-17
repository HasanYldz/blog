from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Topic(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topic")
    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=127, unique=True)
    content = RichTextField()
    status = models.IntegerField(choices=STATUS, default=0)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.title
