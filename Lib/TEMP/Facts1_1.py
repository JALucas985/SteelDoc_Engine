# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 18:48:58 2021

*************************************************************
*************************************************************
********************** BASE DE HECHOS ***********************
*************************************************************
*************************************************************

VERSION 1.0.5

@author: Jorge Lucas


FUNCIONAMIENTO

Aqui se encuentran las clases de las bases de hechos, asi como sus metodos y 
sus atributos
"""

import sqlite3

class BaseHechos:
    
    lSinOrig = []
    lPlaOrig = []
    
    lSinINF = []
    lPlaINF = []
    
    lSinCON = []
    lPlaCON = []
    
    lSolINF = []
    
    lIdCaso = []    #   [ IdCaso  ]
    lIdCasoREPETIDOS = []
    
    """
    lSin = []
    lPla = []
    
    """

    
    def actualizar(self, INFS, INFP, INFSol):
        
        pass
    
    def agregarSintomas(self,lso,lpo):
        
        self.lSinOrig = self.lSinOrig + lso
        self.lPlaOrig = self.lPlaOrig + lpo
        print("Base de hechos actualizada!")
        
    def agregarSintomasINF(self,lso,lpo):
        
        self.lSinINF = self.lSinINF + lso
        self.lPlaINF = self.lPlaINF + lpo
        print("Lista de posibles causas raiz actualizada!")
        print(self.lSinINF)
        
        
    def actualizar_IdCaso(self):
        
        # pass
        
        lAuxID = []
        lAuxIDPOS = []
        lAuxIDREP = []
        
        lAuxSol = []
        lAuxSolPOS = []
        
        
        db_Uni = sqlite3.connect("BC\_Universal.db")
        
        i=0
        while(i < len(self.lSinINF)):            
        
            cursorP = db_Uni.execute("select IdCaso, HC_SOL from Rels where HC_SIN = :HC_SIN and HC_PLA = :HC_PLA",{'HC_SIN':self.lSinINF[i], 'HC_PLA':self.lPlaINF[i]})
        
            CurP = cursorP.fetchall()   #       Obtenemos el IdCaso y la solucion del sintoma inferido
            
            print(CurP)
            
            if(len(CurP) != 0):
                
                lAuxID = lAuxID + [CurP[0][0]]
                lAuxSol = lAuxSol + [CurP[0][1]]
            
            i=i+1
            
        i=0
        while(i < len(lAuxID)):
            
            if(lAuxID[i] not in lAuxIDPOS):
                
                lAuxIDPOS = lAuxIDPOS + [lAuxID[i]]
                lAuxIDREP = lAuxIDREP + [1]
            
            else:
                
                indice = lAuxIDPOS.index(lAuxID[i])
                lAuxIDREP[indice] = (lAuxIDREP[indice])+1
                
            i=i+1
            
        i=0
        while(i < len(lAuxSol)):
            
            if(lAuxSol[i] not in lAuxSolPOS):
                
                lAuxSolPOS = lAuxSolPOS + [lAuxSol[i]]
                
            i=i+1
    
        self.lIdCaso = lAuxIDPOS
        self.lIdCasoREPETIDOS = lAuxIDREP
        self.lSolINF = lAuxSolPOS
    
    
        db_Uni.close()
        
        
    def seleccion(self):
        
        capa_maxima = 3     #   EDITABLE: Maximo numero de niveles de busqueda (aqui ordenas la lista d id y despues seleccionas las soluciones de mayor cantidad)    
        
        lAux = self.lIdCaso
        lAuxREP = self.lIdCasoREPETIDOS
        
        flg = False
        while (flg == False):
            flg = True
            for i in range(len(lAux)-1):
                if lAux[i] > lAux[i+1]:
                    
                    aux1 = lAux[i]
                    aux2 = lAuxREP[i]
                    
                    lAux[i] = lAux[i+1]
                    lAuxREP[i] = lAuxREP[i+1]
                    
                    lAux[i+1] = aux1
                    lAuxREP[i+1] = aux2
                    
                    flg=False
                    
        if (capa_maxima > len(lAux)):    
            
            capa_maxima=len(lAux)
            
        self.lIdCaso = lAux[0:capa_maxima]
        self.lIdCasoREPETIDOS = lAuxREP[0:capa_maxima]
        
        
        print("**Elementos ordenados**")
        print(self.lIdCaso)
        
        db_Uni = sqlite3.connect("BC\_Universal.db")
        
        lAux1 = []
        lAux2 = []
        lAux3 = []
        
        i=0
        while(i<len(self.lIdCaso)):
                
            cursorP = db_Uni.execute("select HC_SIN, HC_PLA, HC_SOL from Rels where IdCaso = :IdCaso",{'IdCaso':self.lIdCaso[i]})
            CurP = cursorP.fetchall()
            print(i)
            print(CurP)
            lAux1=lAux1+[CurP[0][0]] # Sintoma
            lAux2=lAux2+[CurP[0][1]] # Lugar
            lAux3=lAux3+[CurP[0][2]] # Solucion
            i=i+1
        
        
        self.lSinCON = lAux1 
        self.lPlaCON = lAux2 
        self.lSolINF = lAux3
        
        db_Uni.close()
        
        
        
        
        
    def conjuncion(self, arr1_1, arr1_2):
        
        carrlen = len(self.lSinINF)
        carrlen_2 = len(arr1_1)
        
        temp1 = []
        temp2 = []
        
        i = 0
        
        while i < carrlen:
            
            m = 0
            
            
            while m < carrlen_2:
                
                                   
                if (self.lSinINF[i]==arr1_1[m]) and (self.lPlaINF[i]==arr1_2[m]):
                    
                   print("***************************\nSintoma {0} en {1} es igual a {2} en {3}".format(self.lSinINF[i],self.lPlaINF[i],arr1_1[m],arr1_2[m]))
                    
                   temp1.append(arr1_1[m])
                   temp2.append(arr1_2[m])
                    
                   print("CON = {0} en {1}\n**********************************".format(temp1,temp2))
                    
                m = m + 1
                    
            i = i + 1
            
        self.lSinCON = temp1 
        self.lPlaCON = temp2 
        
        
    def eliminarDuplicados(self, arr1, arr2):
        
        # carr1 = arr1
        # carr2 = arr2
        carrlen = len(arr1)
        
        i = 0
        
        while i < carrlen:
            
            m = 0
            
            
            while m < carrlen:
                
                if not(i==m):
                    
                    if (arr1[i]==arr1[m]) and (arr2[i]==arr2[m]):
                    
                        arr1.pop(m)
                        arr2.pop(m)
                        carrlen = len(arr1)
                    
                    else:
                    
                        m = m + 1
                    
                else: 
                    
                    m = m + 1
            i = i + 1
                    
        
        print("Matriz1 = {0}, Matriz 2 = {1}".format(arr1, arr2))
                    
        
        
        
    
    
    
