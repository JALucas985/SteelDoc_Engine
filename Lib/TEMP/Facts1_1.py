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

class BaseHechos:
    
    lSinOrig = []
    lPlaOrig = []
    
    lSinINF = []
    lPlaINF = []
    
    lSinCON = []
    lPlaCON = []
    
    lSolINF = []
    
    
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
                    
        
        
        
    
    
    