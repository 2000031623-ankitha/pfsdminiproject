from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models by default id generated in it


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    #participants=
    updated=models.DateTimeField(auto_now=True) #it will take(timestamp) snapshot for every single updation
    created=models.DateTimeField(auto_now_add=True)# it takes(timestamp) only once it created ---never changes

    class Meta:
        ordering=['-updated','-created'] #without dash(-) it will order in ascending order---newest item will be at the last

    def __str__(self):
        return self.name


class message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE) #on_delete=models.CASCADE is to automatically delete all "child" instances associated with it. This is known as a cascade 
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    