from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_post_list'),
    path('tag/<slug:slug>/', views.TagPostListView.as_view(), name='tag_post_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]