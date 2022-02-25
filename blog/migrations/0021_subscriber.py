# Generated by Django 4.0.2 on 2022-02-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0020_alter_post_related_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
