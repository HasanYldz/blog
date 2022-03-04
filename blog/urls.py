from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('topic/<slug:slug>/', views.TopicDetailView.as_view(), name='topic_detail'),
    path('author/<int:id>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('new-post/', views.AddPostView.as_view(), name='add_post'),
    path('new-topic/', views.AddTopicView.as_view(), name='add_topic'),
    path('edit-post/<slug:slug>/', views.EditPostView.as_view(), name='edit_post'),
    path('newsletter-subscription/', views.SubscriptionView.as_view(), name='newsletter_subscription'),
    path('all-topics/', views.AllTopicsView.as_view(), name='all_topics'),
    path('about/', views.AboutView.as_view(), name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
