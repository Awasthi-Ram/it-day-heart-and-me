from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("heart",views.heart,name='heart'),
    path("heart_predictor",views.heart_predictor,name='heart_predictor'),
    path("register",views.register,name='register'),
]
