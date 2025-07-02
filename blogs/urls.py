from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogDeleteView, BlogDetailView, BlogUpdateView

app_name=BlogsConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/create', BlogCreateView.as_view(), name='create_blogs'),
    path('blogs/detail/<int:pk>/', BlogDetailView.as_view(), name='detail_blogs'),
    path('blogs/update/<int:pk>/', BlogUpdateView.as_view(), name='update_blogs'),
    path('blogs/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blogs'),
]