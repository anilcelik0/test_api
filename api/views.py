from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from . import serializers
from .models import users
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    return render(request,"index.html")

def register(request):

    # if request.method == 'POST':
    #     # fakepp = 'fakepp.jpg'
    #     #öğeleri al
    #     name = request.POST['name']
    #     surname = request.POST['surname']
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     repassword = request.POST['repassword']
    #     email = request.POST['email']
        
    #     user = User.objects.create_user(first_name = name,last_name = surname, username = username, password = password, email = email)
    #     user.save()
    #     return render(request, 'register.html')

    # else:
    #     return render(request, 'register.html')
    
    
    # number=[1,2,3,4,5,6,7,8,9,10]
    # for n in number:
    #     name = "testname"+str(n)
    #     surname = "testsurname"+str(n)
    #     username = "testusername"+str(n)
    #     email = "testemail"+str(n)+"@email.com"
        
    #     user = models.users.objects.create(first_name = name,last_name = surname, username = username, email = email)
    #     user.save()
    return render(request, 'register.html')


@api_view(['GET','POST'])
def User_create_api_view(request):
    
    if request.method == 'GET':
        Users = users.objects.all()
        serializer = serializers.User_Modal(Users, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = serializers.User_Modal(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def User_detail_api_view(request,id):
    try:
        photo_instance = users.objects.get(id=id)
    
    except User.DoesNotExist:
        return Response(
            {
                'errors':404,
                'message':f'böyle bir kullanıcı bulunamadı'
            },
            status=status.status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = serializers.User_Modal(photo_instance)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.User_Modal(photo_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE':
        photo_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
