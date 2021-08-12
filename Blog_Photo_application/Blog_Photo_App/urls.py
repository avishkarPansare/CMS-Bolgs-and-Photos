from django.urls import path
from . import views

urlpatterns = [
    # when user is login then it is open otherwish login/signup only open
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # It is normally open for all
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # login function
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),



    # Delete and update post
    path('updatepost/<int:id>/', views.update_post, name='updatepost'),
    path('delete/<int:id>/', views.delete_post, name='deletepost'),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),


    # Add post 
    path('addBlog/', views.addBlog, name='addBlog'),
    path('addPhoto/', views.addPhoto, name='addphoto'),


]
