from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    isStudent = models.BooleanField(default=True)
    degree_program_or_office = models.CharField(max_length=200)
    profile_picture = models.FileField(blank=True,null=True)
    
    def get_absolute_url(self):
        return reverse('index')
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_text = models.CharField(max_length=200)
    item_photo = models.FileField(blank=True,null=True)
    item_name = models.CharField(max_length=200)
    item_quantity = models.IntegerField(default=0)
    item_condition = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200)
    item_use = models.CharField(max_length=200)