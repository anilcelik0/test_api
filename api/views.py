from operator import truediv
from pickle import TRUE
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from api.serializers import CurrentUserSerializer
from rest_framework import viewsets

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
    #     password = "123.Asd"
    #     repassword = "123.Asd"
    #     email = "testemail"+str(n)+"@email.com"
        
    #     user = User.objects.create_user(first_name = name,last_name = surname, username = username, password = password, email = email)
    #     user.save()
    return render(request, 'register.html')

class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = CurrentUserSerializer