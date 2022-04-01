from django.urls import path
from . import views

urlpatterns = [
    path('', views.CIIndex, name='infracon-index')
]
