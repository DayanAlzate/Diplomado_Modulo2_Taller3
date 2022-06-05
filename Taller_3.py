#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:05:26 2022

@author: dayan
"""
## imporatamos la libreria pandas para poder convertir y interactuar con dataframe  
import pandas as pd
import numpy as np 

class persona():

## ceamos un diccionario que contendra todod los datos recogidos de los estudiantes 

    Datos_estudiantes={"nombre":["dayan alzate hernandez","jesus andres altamiranda","brayan sanchez","daniela hernandez ortiz"],
              "edade" :[25,20,19,27],
              "sexo" :["M","M","M","F"],
              "peso KG" :[85,70,60,65],
              "altura M":[ 1.78,1.70,1.60,1.65],
              "dinero a invertir ":[1000000,2000000,3000000,3000000],
              "interes anual":[0.12,0.20,0.9,0.13],
              "años de inversion":[2,1,3,10],
              "numero telefonico":["+57-3227717091","+57-3116553312","+57-3116777809","+57-3126777239"],
              "Hora de compra del pan":[20,1,17,9]
              }

    ## convertimos el diccionario en un dataframe 
    datos = pd.DataFrame(Datos_estudiantes)
    
        
#Ejercicio 1
    ## metodo que permite calcular el indice de masa corporal
    def calcular_imc(self):
    
         # formula imc
        self.datos["imc"]=self.datos["peso KG"]/self.datos["altura M"]**2
        
        # imprimimos los indice de masa corporal por la terminal con su repectivo mensaje 
 
        for inicio in self.datos["imc"]:
             print ("Tu índice de masa corporales es  "+str(inicio)+" donde 18.5—24.9 es el índice de masa corporal normal \n")
             
        
        
##Ejercicio 2 
    # metodo que calcula las ganacias de invertir su dinero segun los años de invercion  y los intereces anuales 
    def ganancias_invercion(self):
        
        capital_final=0.0
        capital_final=self.datos["dinero a invertir "] *(self.datos["interes anual"]/100+1)**self.datos["años de inversion"]
        self.datos["capital final"]= capital_final
        return capital_final
    
##Ejercicio 3
        
    #metodo que permite calcular el porcentaje de descuento de cada cliente
    def Descuento_Pan(self):
        
        condicion=[
                   (self.datos["Hora de compra del pan"]<= 6),
                   (self.datos["Hora de compra del pan"]> 6)&(self.datos["Hora de compra del pan"]<= 12),
                   (self.datos["Hora de compra del pan"]> 12)&(self.datos["Hora de compra del pan"]<= 18),
                   (self.datos["Hora de compra del pan"]> 18)&(self.datos["Hora de compra del pan"]<= 24)
                  
                  
                   ]
     
        opcion =[0.10,
                 0.20,
                 0.30,
                 0.40
                ]
        
        self.datos["descuento"]= np.select(condicion,opcion)
    
    # metodo que permite calcular el valor de cada pan segun el descuento obtenido anterior mente el metodo anterior  
    def Precio_Pan(self):
        
        self.datos["Percio Pan"]= 15000-(self.datos["descuento"]*15000)
        
#Ejercicio 4
        
    # metodo que permite agregar la extencion al numero telefonico segun su sexo
    def Extencion_Num_Celular(self):
        
        self.datos["Numero Telefonico extencion"]= np.where(self.datos["sexo"]=="M",self.datos["numero telefonico"]+"-11",self.datos["numero telefonico"]+"-10")
        
        

# instanciamos la clase para crear un objeto 
obj_persona= persona()


# con el obj_persona podemos accede a los metodos y atributos de la clase persona 

# llamamos los metodos y atributos necesarios para poder ejecutar nuetro codigo 
obj_persona.calcular_imc()
print (obj_persona.ganancias_invercion())
obj_persona.Descuento_Pan()
obj_persona.Precio_Pan()
obj_persona.Extencion_Num_Celular()
print("tabla de datos ")
print(obj_persona.datos)



     
    
     







