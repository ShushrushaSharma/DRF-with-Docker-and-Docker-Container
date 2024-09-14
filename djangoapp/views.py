from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.

# getting all the users

@api_view(['GET'])
def GetUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# getting a single user

@api_view(['GET'])
def GetUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


# adding users

@api_view(['POST'])
def AddUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# updating users

@api_view(['PUT'])
def UpdateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


# deleting users

@api_view(['DELETE'])
def DeleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()

    return Response("User Deleted Successfully")
