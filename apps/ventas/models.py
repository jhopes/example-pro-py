from django.db import models

# Create your models here.
class Cliente(models.Model):
	"""docstring for ClassName"""
	nombres=models.TextField(max_length=100)
	apellidos = models.TextField(max_length=100)
		