from django.contrib import admin
from .models import users

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','first_name','last_name')
admin.site.register(users,PhotoAdmin)