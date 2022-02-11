from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic)
    title = models.CharField(max_length=256)
    text = models.CharField(max_length=8192)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
        return self.title


