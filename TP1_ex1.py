# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 08:00:00 2023

@author: Paul-Malo
"""
### TP1 PYTHON : PRISE EN MAIN ###


''' 2.1. Présentation

Le calendrier utilisé en France depuis 1582 est le calendrier dit grégorien : 
    • l'année est divisée en 12 mois numérotés de 1 à 12.
    • les mois numéros 1, 3, 5, 7, 8, 10 et 12 ont 31 jours. 
    • Les mois numéros 4, 6, 9 et 11 ont 30 jours. 
    • le mois 2 a 29 jours si l'année est bissextile, 28 jours sinon. 
    • une année est bissextile si 
        o elle ne se termine pas par 00 et est un multiple de 4 
        o ou bien si elle est un multiple de 400.


    2.2) Consignes'''

'1) Écrire une fonction qui teste si une année est bissextile ou non avec la convention suivante : la fonction renvoie la valeur True si l année est bissextile, la valeur False dans le cas contraire.'

def fBis(pAnnee):
    if pAnnee%400==0: #bissextile si multiple de 400
        return True
    elif pAnnee%100!=0 and pAnnee%4==0: #bissextile si multiple de 4 mais pas de 100
        return True
    else:
        return False

'2) Écrire une fonction qui donne le nombre de jours d un mois après avoir vérifié la validité des paramètres. '

def fNbjours(pMois,pAnnee):
    ValRen=0
    if pMois in range(13): #verification de l'existence du mois
        if pMois in [1,3,5,7,8,10,12]: #mois de 31 jours
            ValRen=31
        if pMois==2: #cas particulier de fevrier
            if fBis(pAnnee)==True: #verification de l'annee bissextile avec fBis
                ValRen=29 #29 si bissextile
            else:
                ValRen=28 #28 sinon
        else:
            ValRen=30 #sinon il y a 30 jours
        return ValRen
    else:
        return False


'3) Écrire une fonction qui vérifiera si une date est valide ou non (True signifie date valide, False sinon)'

def fValide(pJour,pMois,pAnnee):
    nbjours=fNbjours(pMois,pAnnee) #recuperation du nombre de jours du mois concerne avec fNbjours
    if nbjours!=False and pJour in range(nbjours+1): #on verifie que le jour est bien compris dans le nombre qu'il y en a dans le mois
        return True
    else:
        return False

'4) Écrire le programme principal qui propose la saisie d une date, la valide et affiche le message "date valide" ou "date non valide" selon le cas.'

jour=int(input("Bonjour, veuillez saisir le numéro du jour :"))     #recuperation des parametres aupres de l'utilisateur
mois=int(input("Veuillez saisir le numéro du mois :"))
annee=int(input("Bonjour, veuillez saisir le numéro de l'année :"))
if fValide(jour,mois,annee)==True:  #appel de la fonction fValide pour verifier que la date existe
    print("Date valide")      #affichage du resultat
else:
    print("Date non valide")
