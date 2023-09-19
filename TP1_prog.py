# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:00:00 2023

@author: Paul-Malo
"""
### TP1 PYTHON : PRISE EN MAIN ###


from TP1_ex1 import *
from TP1_ex2 import *

'Ex 1'

jour = int(input("Bonjour, veuillez saisir le numéro du jour : "))     #recuperation des parametres aupres de l'utilisateur
mois = int(input("Veuillez saisir le numéro du mois : "))
annee = int(input("Bonjour, veuillez saisir le numéro de l'année : "))
if fValide(jour,mois,annee) == True :  #appel de la fonction fValide pour verifier que la date existe
    print("Date valide")      #affichage du resultat
else :
    print("Date non valide")

'Ex 2'

Revenu = int(input("Veuillez entrer votre revenu annuel (en euros) : "))
print("Vous êtes imposables sur votre revenu à hauteur de ", fMesImpots(Revenu), "euros.")