from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('post/<slug:slug>/', views.post_detail.as_view(), name='post_detail')
]
