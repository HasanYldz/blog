# Generated by Django 4.0.2 on 2022-02-11 11:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_alter_post_ti'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ti',
        ),
    ]
