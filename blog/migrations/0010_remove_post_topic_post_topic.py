# Generated by Django 4.0.2 on 2022-02-15 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0009_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='topic',
        ),
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='topic',
                                    to='blog.topic'),
        ),
    ]
