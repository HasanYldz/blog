from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin, HitCount
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


DRAFT = 0
PUBLISHED = 1
STATUS = (
    (DRAFT, "Draft"),
    (PUBLISHED, "Publish")
)


def post_directory_path(instance, filename):
    return 'post_pictures/{0}/{1}'.format(instance.id, filename)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=127, unique=True)
    content = RichTextField()
    status = models.IntegerField(choices=STATUS, default=PUBLISHED)
    pub_date = models.DateTimeField("date published", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    related_posts = models.ManyToManyField('self', blank=True)
    post_picture = models.ImageField(upload_to=post_directory_path, blank=True, null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    def __str__(self):
        return self.title


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    subscription_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class AboutPage(SingletonModel):
    content = RichTextField()

