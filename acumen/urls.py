from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ian', views.ian),
    path('tara', views.ian),
    path('lincoln', views.ian),
]
