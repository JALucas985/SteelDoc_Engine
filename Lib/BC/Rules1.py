# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:14:52 2021


*************************************************************
*************************************************************
********************** BASE DE REGLAS ***********************
*************************************************************
*************************************************************

VERSION 1.0.0

@author: Jorge Lucas


FUNCIONAMIENTO

Se tienen algunas listas de relaciones entre los sintomas indicados y las posibles 
sintomatologias causantes o consecuentes

"""

""" Algunas reglas """

inSint = ""  'Sintoma entrante'
inPlace = "" 'Lugar referente al sintoma entrante'

        

lRelSint = []
lRelPlace = []        

outSol = ""
auxSol = ""



def relacionesSintomas (inS, inP):
    
    inSint = inS
    inPlace = inP
    
    'Representamos el atoramiento en un conveyor'
    
    if ((inSint == "3.1.1.1.0")and(inPlace == "4.0.0.0.0")):
        print("Atoramiento dentro de la maquina")
        lRelSint=["1.0.0.0.0"]
        lRelPlace=["4.1.0.0.0"]
        return(lRelSint)
    
    
    
print(relacionesSintomas("3.1.1.1.0", "4.0.0.0.0"))










