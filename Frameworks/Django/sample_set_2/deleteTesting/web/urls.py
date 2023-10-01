from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('deletePost/<int:post_id>/',views.deletePost,name='deletePost'),
    path('updatePost/<int:post_id>/',views.updatePost,name='updatePost'),
    path('about/',views.about,name='about'),


]
