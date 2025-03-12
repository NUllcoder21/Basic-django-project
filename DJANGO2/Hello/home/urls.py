from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path("",views.index,name='index'),
   path("about",views.about,name='about'),
   path("services",views.services,name='services'),
   path("contect",views.contect,name='contect'),
   path('login/', views.user_login, name='user_login'),
   path("signup",views.signup,name='signup'),
   path('icecream-details/', views.icecream_details, name='icecream_details'),
   path('buy-now/', views.buy_now, name='buy_now'),
  
]
