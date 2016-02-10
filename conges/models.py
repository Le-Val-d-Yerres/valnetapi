from django.db import models

# Create your models here.
class TypeConge(models.Model):
    nom = models.CharField()
    ordre_presentation = models.IntegerField()

class Conge(models.Model):
    debut = models.DateField()
    fin = models.DateField()
    nb_jours = models.FloatField()
    type_conge = models.ForeignKey(TypeConge)