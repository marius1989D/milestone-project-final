from django.db import models
from features.models import Feature
from django.utils import timezone

class Order(models.Model):
	full_name = models.Charfield(max_length=50, blank=False)
	phone_number = models.Charfield(max_length=20, blank=False)
	country = models.Charfield(max_length=40, blank=False)
	post_code = models.Charfield(max_length=20, blank=False)
	town_or_city = models.Charfield(max_length=40, blank=True)
	street_address = models.Charfield(max_length=40, blank=False)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class Order(models.Model):
	order = models.ForeignKey(Order, null=False)
	product = models.ForeignKey(Feature, null=False)
	quantity = models.IntegerField(blank=False)

	def __str__(self):
		return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
