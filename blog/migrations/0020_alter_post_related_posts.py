# Generated by Django 4.0.2 on 2022-02-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0019_alter_post_related_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='related_posts',
            field=models.ManyToManyField(blank=True, to='blog.Post'),
        ),
    ]
