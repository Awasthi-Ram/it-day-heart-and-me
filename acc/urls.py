from django.urls import path
from . import views
urlpatterns = [
    path('', views.signup,name="acc_signup"),
    path('login', views.login,name="acc_login"),
    path('logout', views.logout,name="acc_logout"),
    path('profile', views.profile,name="acc_profile"),
    path('delete', views.delete,name="acc_delete"),
]