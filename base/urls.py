from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"), #"room/<int:pk>/" is the URL pattern that specifies a route for accessing a specific room. <int:pk> is a path converter that matches an integer and stores it in the pk variable. For example, if the URL is "room/3/", then pk would be assigned the value 3.
    path('create-room/',views.createRoom,name="create-room"),
    path('update-room/<str:pk>/',views.updateRoom,name="update-room"),
    path('delete-room/<str:pk>/',views.deleteRoom,name="delete-room"),
]