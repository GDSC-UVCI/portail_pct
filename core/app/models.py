from django.db import models
class Declaration(models.Model):
    id_declaration = models.IntegerField(primary_key=True)
    nom_pr_declare = models.CharField(max_length=255)
    sexe_declare = models.CharField(max_length=10)
    fonct_declare = models.CharField(max_length=50, blank=True)
    date_naiss = models.DateField()
    date_deces = models.DateField()
    mode_declaration = models.CharField(max_length=255)
    raison_deces = models.CharField(max_length=255, blank=True)
    nom_pr_parent = models.CharField(max_length=255)
    lieu_habit = models.CharField(max_length=255)
    def __str__(self):
        return self.nom_pr_

class Deplacement(models.Model):
    id_deplacement = models.IntegerField(primary_key=True)
    nom_pr_deplace = models.CharField(max_length=255)
    sexe_deplace = models.CharField(max_length=10)
    fonct_deplace = models.CharField(max_length=50, blank=True)
    date_naissance = models.DateField()
    provenance = models.CharField(max_length=50)
    mode_heberg = models.CharField(max_length=50)
    lieu_habit = models.CharField(max_length=50)

class RechercheEmploi(models.Model):
    id_offre = models.IntegerField(primary_key=True)
    nom_pr = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    competence = models.CharField(max_length=255)
    contact = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='recherche_emploi/', blank=True)
    message = models.CharField(max_length=255)

class Maladie(models.Model):
    id_maladie = models.IntegerField(primary_key=True)
    nom_maladie = models.CharField(max_length=255)
    periode_maladie = models.DateField()
    des_maladie = models.CharField(max_length=255)

class CentreSante(models.Model):
    id_centre = models.IntegerField(primary_key=True)
    nom_centre = models.CharField(max_length=255)
    emplacement = models.CharField(max_length=255)
    service = models.CharField(max_length=255)

class Pharmacie(models.Model):
    id_pharmacie = models.IntegerField(primary_key=True)
    nom_pharmacie = models.CharField(max_length=255)
    emplacement = models.CharField(max_length=255)
    periode_garde = models.DateField()

class Projets(models.Model):
    id_projet = models.IntegerField(primary_key=True)
    domaine_projet = models.CharField(max_length=255)
    des_projet = models.CharField(max_length=255)

# Create your models here.
