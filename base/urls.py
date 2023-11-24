from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('delete-message/<int:pk>/', views.deleteMesssage, name='delete-message'),
    path('register/', views.registerUser, name='register'),
    path('profile/<int:pk>/', views.userProfile, name='user-profile'),
    path('', views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<int:pk>/', views.deleteRoom, name='delete-room'),

]
