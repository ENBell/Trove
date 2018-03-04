from django.db import models

# Create your models here.


class Room(models.Model):
	name = models.CharField(max_length=50)
	owner = models.CharField(max_length=50)
	level = models.CharField(max_length=50) 
	occupants = models.IntegerField()

	#this function will cause an object to return it's name when queried. ex Room.objects.all() --> <Room: Master Bedroom>
	def __str__(self):
		return self.name

class Person(models.Model):
	name = models.CharField(max_length=50)
	height = models.IntegerField()
	weight = models.IntegerField()
	eye_color = models.CharField(max_length=10)