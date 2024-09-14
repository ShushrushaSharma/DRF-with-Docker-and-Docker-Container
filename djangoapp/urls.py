from django.urls import path
from .views import GetUser, GetUsers, AddUser, UpdateUser, DeleteUser

urlpatterns = [
    path('', GetUsers, name='getUsers'),
    path('getuser/<int:pk>', GetUser, name='getUser'),
    path('adduser/', AddUser, name='addUser'),
    path('updateuser/<int:pk>/', UpdateUser, name='updateUser'),  
    path('deleteuser/<int:pk>/', DeleteUser, name='deleteUser'), 
]
