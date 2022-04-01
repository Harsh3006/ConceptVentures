from django.urls import path
from .views import BlogListView, BlogDetailView, CategoryView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog"),
    path('<slug:slug>', BlogDetailView.as_view(), name="blog-detail"),
    path('category/<str:category>', CategoryView, name="category"),
]
