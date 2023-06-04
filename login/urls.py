from django.contrib import admin
from django.urls import path, include
from login import views
urlpatterns = [
    path('', views.index_, name="index"),
    path('logins', views.loginUser, name="logins"),
    path('logout', views.logoutUser, name="logout"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('food_request', views.food_request, name="food_request"),
    path('home', views.home, name="home"),
    path('laundary_page', views.laundary_page, name="laundary_page"),
    path('leave', views.leave, name="leave"),
    path('mess', views.mess, name="mess"),
    path('photos', views.photos, name="photos"),
    path('services', views.services, name="services"),
    # path('contact_enq', views.contact_enq, name="contact_enq"),
    # path('food_enq', views.food_enq, name="food_enq"),
] 