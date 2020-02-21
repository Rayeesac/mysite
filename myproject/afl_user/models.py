from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Newsletter(models.Model):
	email = models.EmailField(max_length=255,unique=True)
	class Meta:
		db_table = "newsletter"

class Contact(models.Model):
	first_name = models.CharField(max_length=255,blank=False)
	last_name = models.CharField(max_length=255,blank=False)
	email = models.EmailField(max_length=255,blank=False)
	phoneno = models.CharField(max_length=12,)
	msg =models.CharField(max_length=300,blank=False)
	class Meta:
		db_table = "Contact"		  

class Country(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
    	db_table = 'Country'

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
    	db_table = "State"

    def __str__(self):
        return self.name

class Profile(models.Model):
	uid = models.IntegerField()
	img = models.ImageField(upload_to='profile/', null=True, blank=True)
	address = models.CharField(max_length=500, blank=True)
	country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
	state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
	pin = models.CharField(max_length=6,null=True)
	DOB = models.DateField(null=True)
	
	class Meta:
		db_table = "Profile"

	def __str__(self):
		return self.name