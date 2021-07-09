from django.urls import path

from . import views

urlpatterns = [
    path('',views.idol_index),
    path('<int:id>',views.idol_show)
]
