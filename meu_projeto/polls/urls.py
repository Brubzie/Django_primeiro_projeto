from django.urls import path
from . import views

urlpatterns = [ # Padrões de URLs
    path('', views.index, name = 'index')
]