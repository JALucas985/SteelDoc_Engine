# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:40:02 2021

*************************************************************
*************************************************************
******************** MOTOR DE INFERENCIA ********************
*************************************************************
*************************************************************

VERSION 1.0.5

@author: Jorge Lucas


FUNCIONAMIENTO

Se adquieren sintomas del problema inicial y se procesan navegando entre las 
reglas de la base de conocimientos

"""

from BC.Rules1_1 import *
from TEMP.Facts1_1 import *


lTEMPS = []
lTEMPP = []

Bh1 = BaseHechos()

"""

# Entrada por consola (comentar cuando se usa en modular)
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
            
"""

class Inferencia:
    
    
    ltS = []
    ltP = []
    ltSol = []
    
    lINFS = []
    lINFP = []
    lINFSol = []
    
    lINF1S = []
    lINF1P = []
    
    Sbh = BaseHechos()
    
    
    
    def __init__ (self,tS,tP,bh):
        
        self.ltS = [tS]
        self.ltP = [tP]
        self.Sbh = bh
        self.Sbh.agregarSintomas(self.ltS,self.ltP)
        
    def modTol(self):
        
        pass
    
        
    
    def modPon(self,lS,lP,mode):
        
        # pass
        
        if mode == 0: #     Modo para visualizar todas las causas raiz
            l=0
            for i in lS:
            
                MetaSintoma = VectorSintoma(lS[l],lP[l])
                MetaSintoma.buscarSintomasRaiz()
                self.Sbh.agregarSintomasINF(MetaSintoma.lRelSintRoot, MetaSintoma.lRelPlaceRoot)
                l=l+1
                self.Sbh.eliminarDuplicados(self.Sbh.lSinINF, self.Sbh.lPlaINF)
        
        elif mode == 1: #     Modo para inferencia real
            # print("Entrando al elif")
            l=0
            for i in lS:
                
                # print (i)
            
                if l==0:
                    MetaSintoma = VectorSintoma(lS[l],lP[l])
                    MetaSintoma.buscarSintomasRaiz()
                    self.Sbh.agregarSintomasINF(MetaSintoma.lRelSintRoot, MetaSintoma.lRelPlaceRoot)
                    l=l+1
                    self.Sbh.eliminarDuplicados(self.Sbh.lSinINF, self.Sbh.lPlaINF)
                    print("Primera vez !!!! {0} en {1}".format(self.Sbh.lSinINF, self.Sbh.lPlaINF))
                    
                else:
                    MetaSintoma = VectorSintoma(lS[l],lP[l])
                    MetaSintoma.buscarSintomasRaiz()
                    self.Sbh.conjuncion(MetaSintoma.lRelSintRoot,MetaSintoma.lRelPlaceRoot)
                    self.Sbh.eliminarDuplicados(self.Sbh.lSinCON, self.Sbh.lPlaCON)
                    if self.Sbh.lSinCON == []:
                        
                        print("Despues de la conjuncion no existen valores coincidentes: \nSintomas inferidos: {0} en {1}".format(self.Sbh.lSinCON,self.Sbh.lPlaCON))
                        
                        
                    else:
                        
                        print("Despues de la conjuncion: \nSintomas inferidos: {0} en {1}".format(self.Sbh.lSinCON,self.Sbh.lPlaCON))
                        self.lINF1S = self.lINF1S + self.Sbh.lSinCON
                        self.lINF1P = self.lINF1P + self.Sbh.lPlaCON
                        
                    l=l+1
    
"""

Sintoma2 = VectorSintoma("1.1.1.0.0", "4.1.1.0.0")
Sintoma2.buscarSintomasConsecuencia()
print(Sintoma2.lRelPlace)
Sintoma2.buscarSintomasRaiz()
Sintoma2.solucionRelativa()



Inf1 = Inferencia(lTEMPS, lTEMPP, Bh1)
Inf1.modPon(lTEMPS, lTEMPP, 1)


# print(Bh1.lSinINF)

"""