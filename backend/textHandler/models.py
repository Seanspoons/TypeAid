from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class textfield(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

 
