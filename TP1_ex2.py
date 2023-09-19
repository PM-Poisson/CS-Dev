# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:00:00 2023

@author: Paul-Malo
"""
### TP1 PYTHON : PRISE EN MAIN ###


'''3. Montant de l'impôt d'une personne célibataire :

Consigne : Implémenter une fonction def fMesImpots(revenu): qui calcule le montant de l'impôt sur le revenu d'une 
personne seule. Le programme principal demandera à l'utilisateur le montant de ses revenus et appellera 
ladite fonction avant de faire un affichage.'''

def fMesImpots(revenu) :
    ValRen = 0 #initialisation de la valeur des impots
    tranches = {160336 : 45 , 74545 : 41 , 26070 : 30 , 10225 : 11} #creation du dico répertoriant les tranches et leurs pourcentages
    for i,val in tranches.items() : #parcours du dico
        if revenu - i >= 0 : #si on fait partie de la tranche en cours
            ValRen += (revenu - i) * val / 100 #on ajoute le montant d'impots correspondant
            revenu = i #et on deduit la somme imposee des revenus
    ValRen = int(ValRen) #troncature à l'euro près
    return ValRen