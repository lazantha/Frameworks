from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='page_home'),
    path('register/', views.createStudent,name='register'),
    path('sub_reg/', views.subjectReg,name='sub_reg'),
    path('admin_reg/', views.adminRegister,name='admin_reg'),
    
    
    
    
    # path('contact/', views.contact,name='page_contact'),
    # path('about/', views.about,name='page_about'),
    



]
