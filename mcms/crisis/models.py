from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    
    
class Device(models.Model):
    phone_number = models.CharField(max_length=30)
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    
    
class Location(models.Model):
    phone_id = models.ForeignKey(Device,on_delete=models.CASCADE)
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    update_time = models.DateTimeField(auto_now=True)
    
    
class Team(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    color = models.CharField(max_length=10)
    responsible_actor= models.ForeignKey(Actor, on_delete=models.PROTECT)
    
    
class Team_actor(models.Model):
    actor_id = models.ForeignKey(Actor,on_delete=models.PROTECT )
    team_id = models.ForeignKey(Team,on_delete=models.PROTECT)
    



