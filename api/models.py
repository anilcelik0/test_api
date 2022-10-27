from django.db import models

# Create your models here.


class users(models.Model):
    id = models.AutoField(primary_key=True,null=False,unique=True)
    username = models.CharField(null=False, max_length=50)
    email = models.CharField(null=False, max_length=150)
    first_name = models.CharField(null=False, max_length=150)
    last_name = models.CharField(null=False, max_length=150)
    