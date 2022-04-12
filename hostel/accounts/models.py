from django.db import models

# Create your models here.
class Inmates(models.Model):
	Hostel_ID = models.CharField(max_length=30, null=True)
	Name = models.CharField(max_length=100, null=True)
	Room_Num = models.CharField(max_length=10, null=True)
	Preference = models.CharField(max_length=20, null=True)
	Bill_Amount = models.IntegerField(null=True)
	MC = models.IntegerField(null=True)
	Marked = models.IntegerField(null=True)