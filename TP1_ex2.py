# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 10:00:00 2023

@author: Paul-Malo
"""
### TP1 PYTHON : PRISE EN MAIN ###


'''3. Montant de l'impôt d'une personne célibataire :

Consigne : Implémenter une fonction def fMesImpots(revenu): qui calcule le montant de l'impôt sur le revenu d'une 
personne seule. Le programme principal demandera à l'utilisateur le montant de ses revenus et appellera 
ladite fonction avant de faire un affichage.

10225 0
26070 11
74545 30
160336 45'''

def fMesImpots(revenu):
    ValRen=0
    tranches={10225:0,26070:11,74545:30,160336:45}