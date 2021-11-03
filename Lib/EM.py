# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:44:42 2021

*************************************************************
*************************************************************
****************** MOTOR DE EXPLICACIONES *******************
*************************************************************
*************************************************************

VERSION 1.0.5

@author: Jorge Lucas


FUNCIONAMIENTO

Aqui se encuentran las traducciones ante el lenguaje maquina, para lo cual 
usaremos las base de datos creadas en SQLite

@author: Jorge Lucas
"""

import sqlite3
from IM import *

lTEMPS = []
lTEMPP = []


vent1 = 1

while (vent1 == 1):

    vent2 = 1
    
    auxS = input ("Sintoma: ")
    auxP = input ("Lugar: ")
    
    lTEMPS = lTEMPS + [auxS]
    lTEMPP = lTEMPP + [auxP]
    
    while (vent2 == 1):
        
        aux = input ("Mas sintomas? - 1. Si      0. No")
        if aux == "1":
            vent2 = 0
        elif aux == "0":
            vent2 = 0
            vent1 = 0
        else:
            print ("Parametro no reconocido .-.")
            


Inf1 = Inferencia(lTEMPS, lTEMPP, Bh1)
Inf1.modPon(lTEMPS, lTEMPP, 1)

# auxS = input ("Homoclave de sintoma: ")


db_Sin = sqlite3.connect("BC\Sint.db")
db_Pla = sqlite3.connect("BC\Parts.db")

l = 0

lenSin=len(Inf1.Sbh.lSinCON)

print("Sintomas ")

while l < lenSin:

    auxS = Inf1.Sbh.lSinCON[l]
    auxP = Inf1.Sbh.lPlaCON[l]
    
    # print("*************{0} en {1}*******************".format(auxS, auxP))
    
    cursorS = db_Sin.execute("select Clase, SubClase, Sintoma1, Sintoma2, Sintoma3 from Sintomas where Homoclave = ?",(auxS,))
    cursorP = db_Pla.execute("select Clase, SubClase, Lugar1, Lugar2, Lugar3 from Lugar where Homoclave = ?",(auxP,))
    
    
    for row in cursorS:
    
        print(" {0}".format(row))
    
    
    
    for row2 in cursorP:
        
        
        print(" en {0},".format(row2))
    
    
    
    l=l+1

print(" han sido devueltos como causa raiz")

"""
for row in cursorS:
    
    print(row)
    
for row in cursorP:
    
    print(row)
    
"""

db_Sin.close()
db_Pla.close()




