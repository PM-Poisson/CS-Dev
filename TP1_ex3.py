# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:00:00 2023

@author: Paul-Malo
"""
### TP1 PYTHON : PRISE EN MAIN ###

### Ex 3 ###


'''Consigne : Vous devrez écrire une fonction def fmultiplication(): qui prend deux paramètres (un pour chaque 
matrice à multiplier) et qui retourne le résultat. On travaillera avec des listes de listes.'''

def fMultiplication(pMat1,pMat2) :
    ValRen = []
    if len(pMat1) == len(pMat2[0]) :
        for i in range(len(pMat1)) :
            ligne = pMat1[i]
            colonne = []
            for j in range(len(pMat2[0])) :
                colonne.append = pMat2[j[i]]
                
    return ValRen