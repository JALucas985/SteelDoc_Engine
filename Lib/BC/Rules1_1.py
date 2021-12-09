# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 17:14:52 2021


*************************************************************
*************************************************************
********************** BASE DE REGLAS ***********************
*************************************************************
*************************************************************

VERSION 1.0.5

@author: Jorge Lucas


FUNCIONAMIENTO

Se tienen algunas listas de relaciones entre los sintomas indicados y las posibles 
sintomatologias causantes o consecuentes

"""

""" Algunas reglas """


import sqlite3


inSint = ""  #'Sintoma entrante'
inPlace = "" #'Lugar referente al sintoma entrante'

        




class VectorSintoma:
    
    
    lRelSint = []
    lRelPlace = []
    
    lRelSintRoot = []
    lRelPlaceRoot = []
    
    lRelSolO = []
    lRelPlaO = []   
    
    lIdCaso = []    #   [ IdCaso ]

    outSol = ""
    auxSol = ""
    
    
    
    def __init__(self, inS, inP):
    
        self.inS = inS
        self.inP = inP
        
        
    def varClean(self):
        
        self.lRelSint = []
        self.lRelPlace = []
        
        self.lRelSintRoot = []
        self.lRelPlaceRoot = []

        self.lRelSolO = []
        self.lRelPlaO = []     

        self.lIdCaso = []
        
        self.outSol = ""
        self.auxSol = ""
        
    def buscarSintomasConsecuencia(self):
        
        lAuxS = []
        lAuxP = []
        
        if self.inS == "3.1.1.1.0":                      #***Buscando el atoramiento***
            
            if self.inP == "4.0.0.0.0":                   # En conveyor
            
                lAuxS = ["1.0.0.0.0"]
                lAuxP = ["4.1.0.0.0"]
                
            elif self.inP == "4.1.1.0.0":
                
                lAuxS = ["1.0.0.0.0"]
                lAuxP = ["4.1.0.0.0"]
                
                
        
        
        else:
            
            lAuxS = ["0.0.0.0.0"]
            lAuxP = ["0.0.0.0.0"]
        
        
        self.lRelSint = self.lRelSint + lAuxS
        self.lRelPlace = self.lRelPlace + lAuxP
                
        print("Resultados: Sintoma {0} en {1} pueden ser consecuentes".format(self.lRelSint, self.lRelPlace))    
         
        # pass
    
    
    def buscarSintomasRaiz1(self):
        
        lAuxS = []
        lAuxP = []
    
        db_Uni = sqlite3.connect("BC\_Universal.db")
        
        cursorP = db_Uni.execute("select IdCaso, HC_SOL from Rels where HC_SIN = :HC_SIN and HC_PLA = :HC_PLA",{'HC_SIN':self.inS, 'HC_PLA':self.inP})
        
        CurP = cursorP.fetchall()   #       Obtenemos el IdCaso del sintoma original
        
        print(len(CurP))
        print(CurP)
        
        if(len(CurP) == 0):
            
            print("Este sintoma no existe")
            lAuxS = ["0.0.0.0.0"]
            lAuxP = ["0.0.0.0.0"]
        
        else:
        
            cursorS = db_Uni.execute("select IdRoot from CausaRaiz where IdCaso = :IdCaso",{'IdCaso':CurP[0][0]})
        
            CurS = cursorS.fetchall()   #       Obtenemos el IdCaso de la raiz
            
            if(CurS[0][0] != 0):    #       Si el sintoma caso no es una causa raiz
                
            
                i=0
            
                while(i<len(CurS)):
            
                    # print(len(CurS))
                    print(i)
                    print(CurS[i][0])
                    self.lIdCaso = self.lIdCaso + [CurS[i][0]]
                    cursorP = db_Uni.execute("select HC_SIN, HC_PLA from Rels where IdCaso = :IdCaso ",{'IdCaso':CurS[i][0]}) 
                    CurP = cursorP.fetchall()   #       Obtenemos las variables del sintoma raiz
                    print(CurP)
                
                    lAuxS = lAuxS + [CurP[0][0]]
                    lAuxP = lAuxP + [CurP[0][1]]
                    
                
                    i=i+1
            else:
                
                lAuxS = ["0.0.0.0.0"]
                lAuxP = ["0.0.0.0.0"]
            
                    
        self.lRelSintRoot = self.lRelSintRoot + lAuxS
        self.lRelPlaceRoot = self.lRelPlaceRoot + lAuxP
                
        print("Resultados: Sintoma {0} en {1} pueden ser causa raiz para {2} en {3}".format(self.lRelSintRoot, self.lRelPlaceRoot, self.inS, self.inP))    
         
        # pass        
        
        db_Uni.close()
    
    
    def buscarSintomasRaiz(self):
        
        lAuxS = []
        lAuxP = []
        
        
        
        if self.inS == "1.1.1.0.0":                      #***Buscando el ruido***
            
            if self.inP == "4.1.1.0.0":                   
            
                lAuxS = ["3.1.1.0.0","3.1.1.0.0","5.3.0.0.0","5.3.0.0.0","5.4.0.0.0","5.4.0.0.0","4.1.0.0.0"]
                lAuxP = ["4.1.0.0.0","6.2.0.0.0","6.2.0.0.0","4.1.2.0.0","6.2.0.0.0","6.2.3.0.0","6.2.0.0.0"]
                
            elif self.inP == "4.1.0.0.0":
                
                lAuxS = ["1.0.0.0.0","5.3.0.0.0","5.4.0.0.0","5.4.0.0.0"]
                lAuxP = ["4.1.0.0.0","4.1.2.0.0","6.2.0.0.0","6.2.3.0.0"]
        
        elif self.inS == "3.1.1.0.0":                      #***Buscando el atoramiento***
            
            if self.inP == "4.0.0.0.0":                   # En conveyor
            
                lAuxS = ["3.1.3.1.0","3.1.3.2.0","3.1.2.1.0","5.3.0.0.0","5.4.0.0.0"]
                lAuxP = ["4.1.1.0.0","4.1.1.0.0","4.1.0.0.0","4.1.0.0.0","4.1.0.0.0"]
                
            elif self.inP == "4.1.0.0.0":
                
                lAuxS = ["1.0.0.0.0"]
                lAuxP = ["4.1.0.0.0"]
                
                
        elif self.inS == "4.1.3.0.0":
            
            if self.inP == "6.2.1.0.0" or self.inP == "4.1.2.0.0" or self.inP == "4.1.1.0.0":                   # En suelo de conveyor
            
                lAuxS = ["5.1.1.0.0"]
                lAuxP = ["4.1.1.0.0"]
                
            elif self.inP == "":
                
                lAuxS = ["1.0.0.0.0"]
                lAuxP = ["4.1.0.0.0"]
            
        
        else:
            
            lAuxS = ["0.0.0.0.0"]
            lAuxP = ["0.0.0.0.0"]
        
        self.lRelSintRoot = self.lRelSintRoot + lAuxS
        self.lRelPlaceRoot = self.lRelPlaceRoot + lAuxP
                
        print("Resultados: Sintoma {0} en {1} pueden ser causa raiz para {2} en {3}".format(self.lRelSintRoot, self.lRelPlaceRoot, self.inS, self.inP))    
         
        # pass
    
    
    def solucionRelativa(self):
        
        lAuxSolO = []
        lAuxPlaO = []
        
        if self.inS == "3.1.1.1.0":                      #***Buscando solucion al atoramiento***
            
            if self.inP == "4.0.0.0.0":
                
                lAuxSolO = ["16.2.0"]
                lAuxPlaO = ["4.1.0.0.0"]
                
                
        elif self.inS == "4.1.3.0.0":
            
            if self.inP == "6.2.1.0.0" or self.inP == "4.1.2.0.0" or self.inP == "4.1.1.0.0": 
                
                lAuxSolO = ["18.0.0"]
                lAuxPlaO = ["4.1.1.0.0"]
                
        else:
            
            lAuxSolO = ["0.0.0.0.0"]
            lAuxPlaO = ["0.0.0.0.0"]
        
                
        self.lRelSolO = self.lRelSolO + lAuxSolO
        self.lRelPlaO = self.lRelPlaO + lAuxPlaO
        
        print("Resultados: Soluciones para el Sintoma {0} en {1} pueden ser {2} en {3}".format(self.inS, self.inP,self.lRelSolO,self.lRelPlaO))    
        
        # pass
    
"""   
Sintoma1 = VectorSintoma("4.1.3.0.0", "4.1.1.0.0")
Sintoma1.buscarSintomasConsecuencia()
print(Sintoma1.lRelPlace)
Sintoma1.buscarSintomasRaiz()
Sintoma1.solucionRelativa()


Sintoma2 = VectorSintoma("1.1.1.0.0", "4.1.1.0.0")
Sintoma2.buscarSintomasConsecuencia()
print(Sintoma2.lRelPlace)
Sintoma2.buscarSintomasRaiz()
Sintoma2.solucionRelativa()
"""
    
