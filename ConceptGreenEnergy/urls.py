from django.urls import path
from . import views

urlpatterns = [
    path('', views.CGEIndex, name='cge-index')
]