from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('menu/<str:food>/', views.food_detail)
]
