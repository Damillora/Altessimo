from django.urls import path

from . import views

urlpatterns = [
    path('',views.artist_index),
    path('<slug:slug>',views.artist_show)
]
