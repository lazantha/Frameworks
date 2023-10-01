from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homePage'),
    path('read/',views.read,name='readPage'),
    path('dyna/<int:pk>/',views.dynamicUrl,name='dynamic'),




       
]
