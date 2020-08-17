from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('/<int:category_id>/posts', views.category_detail, name='category_detail'),
    path('posts/about', views.about, name='about'),
]