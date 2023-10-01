from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home_page'),
    path('form/', views.form,name='form_page'),
    path('userReg/', views.userReg,name='userReg'),
        


]
