from django.db import models
from django.contrib import admin


class Participant(models.Model):


	nume = models.CharField(max_length=50)
	prenume = models.CharField(max_length=50)
	institutie = models.CharField(max_length=50)
	judet = models.CharField(max_length=50)
	localitate = models.CharField(max_length=50)
	informatica = models.BooleanField(default=False)
	tic = models.BooleanField(default=False)
	motiv = models.TextField()
	email = models.EmailField(max_length=100, unique = True)
	prezentari = models.BooleanField(default=False)
	workshop = models.BooleanField(default=False)
	token = models.CharField(max_length=16)
	confirmed = models.BooleanField(default=False)

	def __str__(self):

		return self.nume + " - " + self.prenume + " | " + self.email






admin.site.register(Participant)