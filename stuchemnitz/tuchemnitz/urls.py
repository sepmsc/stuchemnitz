from django.contrib import admin
from django.urls import path, include
from tuchemnitz import views

# URL configuration for the stuchemnitz project. 
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chemnitz/', views.chemnitz, name='chemnitz'),
    path('tuchemnitz/', views.tuchemnitz, name='tuchemnitz'),
    path('dormitory/', views.dormitory, name='dormitory'),
    path('contactus/', views.contact, name='contactus'),
    path('news/', views.news, name='news'),
    path('conversations/', views.conversations, name='conversations'),
    path('submit/', views.submitview, name='submitview'),

]
