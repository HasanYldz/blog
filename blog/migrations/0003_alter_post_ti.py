# Generated by Django 4.0.2 on 2022-02-11 11:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_post_ti'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ti',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
