from django.urls import path

from . import views

urlpatterns = [
    path('categories',views.category_index),
    path('categories/<slug:slug>',views.category_show),
    path('branches',views.branch_index),
    path('branches/<str:acronym>',views.branch_show),
]
