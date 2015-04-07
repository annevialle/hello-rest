from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Box(models.Model):
	name = models.CharField(max_length=200, blank=True)
	spin = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Hello(models.Model):
	boxSender = models.ForeignKey(Box, related_name='boxSender')
	boxReceiver = models.ForeignKey(Box, related_name='boxReceiver')
	date = models.DateTimeField(default=datetime.datetime.now)

