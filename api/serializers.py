from django.contrib import auth
from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import users


class User_Modal(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username','first_name','last_name')
