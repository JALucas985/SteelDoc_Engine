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


lActINF = []
# lPlaINF = []

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
Inf1.modPon(lTEMPS, lTEMPP, 2)

# auxS = input ("Homoclave de sintoma: ")


# db_Pla = sqlite3.connect("BC\Parts.db")
db_Sin = sqlite3.connect("BC\_Universal.db")
# db_Pla = sqlite3.connect("BC\_Universal.db")

l = 0

lenSin=len(Inf1.Sbh.lSinCON)

print("\n\n\n\n--------------Sintomas--------------\n\n")

while l < lenSin:

    auxS = Inf1.Sbh.lSinCON[l]
    auxP = Inf1.Sbh.lPlaCON[l]
    
    # print("*************{0} en {1}*******************".format(auxS, auxP))
    
    cursorS = db_Sin.execute("select TRAD_Sin from Sintomas where Homoclave = ?",(auxS, ))
    cursorP = db_Sin.execute("select TRAD_Pla from Lugar where Homoclave = ?",(auxP,))
    
    dCurS = cursorS.fetchall()
    dCurP = cursorP.fetchall()
    
    
    
    print("Una posible causa raiz de estos problemas es {0} en {1}, ".format(dCurS[0][0],dCurP[0][0]))
    
    cursorS = db_Sin.execute("select IdCaso, HC_SOL from Rels where HC_Sin = :HC_Sin AND HC_Pla = :HC_Pla",{'HC_Sin':auxS, 'HC_Pla':auxP})
    
    dCurS = cursorS.fetchall()
    
    # print(dCurS)
    
    cursorP = db_Sin.execute("select TRAD_A, TRAD_Pla from VW_SolucionRelativa_TRAD where IdSOL = :IdSOL",{'IdSOL':dCurS[0][1]})
    
    dCurP = cursorP.fetchall()
    
    # lActINF[][]
    
    print(" coincide con el IdCaso {0}".format(dCurS[0][0]))
    
    print("*** la solucion relativa para este sintoma es: ***")
    
    i=0
    for row in dCurP:
        
        print("{0} en {1}, ".format(dCurP[i][0],dCurP[i][1]))
        i=i+1
    
    l=l+1

print("\n\n ***Buen Dia***")



"""
for row in cursorS:
    
    print(row)
    
for row in cursorP:
    
    print(row)
    
"""

db_Sin.close()
# db_Pla.close()




