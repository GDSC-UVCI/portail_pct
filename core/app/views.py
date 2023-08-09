from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Declaration, Deplacement, RechercheEmploi, Maladie, CentreSante, Pharmacie, Projets
def declaration_list(request):
    declarations = Declaration.objects.all()
    return render(request, 'app/declaration_list.html', {'declarations': declarations})

def deplacement_list(request):
    deplacements = Deplacement.objects.all()
    return render(request, 'deplacement_list.html', {'deplacements': deplacements})

def recherche_emploi_list(request):
    recherches_emploi = RechercheEmploi.objects.all()
    return render(request, 'recherche_emploi_list.html', {'recherches_emploi': recherches_emploi})

def maladie_list(request):
    maladies = Maladie.objects.all()
    return render(request, 'maladie_list.html', {'maladies': maladies})

def centre_sante_list(request):
    centres_sante = CentreSante.objects.all()
    return render(request, 'centre_sante_list.html', {'centres_sante': centres_sante})

def pharmacie_list(request):
    pharmacies = Pharmacie.objects.all()
    return render(request, 'pharmacie_list.html', {'pharmacies': pharmacies})

def projets_list(request):
    projets = Projets.objects.all()
    return render(request, 'projets_list.html', {'projets': projets})

# Create your views here.
