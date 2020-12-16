from django.urls import path

from . import views

urlpatterns = [
    path('',views.song_index),
    path('<int:id>',views.song_id),
    path('<int:id>/<str:title>',views.song_show),
]
