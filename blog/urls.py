from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('post/<slug:slug>/', views.post_detail.as_view(), name='post_detail'),
    path('topic/<slug:slug>/', views.topic_detail.as_view(), name='topic_detail'),
    path('author/<int:id>/', views.author_detail.as_view(), name='author_detail'),
    path('new-post/', views.add_post.as_view(), name='add_post'),
    path('new-topic/', views.add_topic.as_view(), name='add_topic'),
    path('edit-post/<slug:slug>/', views.edit_post.as_view(), name='edit_post'),
]
