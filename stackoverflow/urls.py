from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='stackoverflow-home'),
    path('about/', views.about, name='stackoverflow-about'),
]
