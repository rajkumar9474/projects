from django.contrib import admin
from django.urls import path,include
from main_app import views

urlpatterns = [
    path('',views.home),
    
    path('index/',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('donate_blood/',views.donate_blood,name='donate_blood')
]