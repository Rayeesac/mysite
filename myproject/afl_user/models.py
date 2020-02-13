from django.db import models

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