from django.urls import path
from . import views

urlpatterns = [
    path('declarations/', views.declaration_list, name='declaration_list'),
    path('deplacements/', views.deplacement_list, name='deplacement_list'),
    path('recherches_emploi/', views.recherche_emploi_list, name='recherche_emploi_list'),
    path('maladies/', views.maladie_list, name='maladie_list'),
    path('centres_sante/', views.centre_sante_list, name='centre_sante_list'),
    path('pharmacies/', views.pharmacie_list, name='pharmacie_list'),
    path('projets/', views.projets_list, name='projets_list'),
]
