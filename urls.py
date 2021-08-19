from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='evaluation-home'),
    path('form/',views.form,name='evaluation-form'),#view.py e form name e mathod create korechi
    path('',views.index,name='evaluation-index'),
    path('regi/',views.regi,name='evaluation-regi'),
    path('logout/',views.logout,name='evaluation-logout'),
    path('faculty/',views.faculty,name='evaluation-faculty'),
    
   
  
  
]
