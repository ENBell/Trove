from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ian', views.ian),
    path('tara', views.tara),
    path('lincoln', views.ian),
    path('acubox', views.acubox)
]
