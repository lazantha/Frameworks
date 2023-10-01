from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home_page'),
    path('content/', views.content,name='content_page'),
    path('about/', views.about,name='about_page'),
    path('join/', views.join,name='join_page'),
    
    
    
    
       
]
