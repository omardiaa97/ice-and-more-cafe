from django.views.generic import RedirectView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]