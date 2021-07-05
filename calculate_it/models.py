from django.conf import settings
from django.db import models


class Person(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"


class House(models.Model):
	rent = models.IntegerField(null=True)
	servicecosts = models.IntegerField(null=True)
	total_rent = models.IntegerField(null=True)
	gas = models.IntegerField(null=True)
	electricity = models.IntegerField(null=True)

	def __str__(self):
		return f"House {self.id}: Rent = {self.rent}, Servicecosts = {self.servicecosts}"

