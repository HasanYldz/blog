# Generated by Django 4.0.2 on 2022-02-16 09:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_topic_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]