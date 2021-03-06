# Generated by Django 4.0.2 on 2022-03-03 09:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_post_post_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=1),
        ),
    ]
