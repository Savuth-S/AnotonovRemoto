# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 03:07:25 2020

@author: Savuth S.
"""
###Funciones
def calc_Precio(p,d,i,m): #Variables en orden respectivo: Peso del paquete, Distancia del vuelo, Internacionalidad del vuelo, Mostrar mensajes de descuento
    "Función para calcular el precio del vuelo"
    
    #Declaración de variables
    des = 1 #Descuento a aplicar
    
    if i == 1:
        if d > 4971 and p > 400: #Se convirtio el valor del enunciado del ejercicio a millas
            des = 0.90
            
            if m == True:
                print("Se ha aplicado un descuento por distancia y peso de carga, precio sin alterar: $"+ str(4500*p+8000*d)+"\n")
            
        pf = (4500*p+8000*d)*des
    else:
         if p > 100:
            des = 0.85
            
            if m == True:
                print("\nSe ha aplicado un descuento por peso de carga, precio sin alterar: $"+ str(4500*p+8000*d)+"\n")

         pf = ((4500*p)*des)+4000*d
        
    return pf

###Programa principal

#Declaración de variables
p_total = 0#Peso total del paquete
pre_total = 0#Precio total

while p_total < 640000:
    #Declaración de variables
    p_paquete = 0#Peso del paquete individual
    inter = 0#Internacionalidad
    dis = 0#Distancia del vuelo
    
    while p_paquete < 10:
        p_paquete = float(input("Ingrese el peso del paquete en kilogramos, debe ser mayor a 10kgs: "))
    while inter > 2 or inter < 1:
        inter = int(input("¿Es vuelo internacional? \n1 - Sí \n2 - No \n"))
    
    if inter == 1:
        dis = float(input("Ingrese la distancia del vuelo en millas: "))
    else:
        dis = float(input("Ingrese la distancia del vuelo en kilometros: "))
        
    print("\nEl precio del paquete es: $"+ str(calc_Precio(p_paquete,dis,inter,True)))
    pre_total = calc_Precio(p_paquete,dis,inter,False)
    p_total += p_paquete
    
print("\n\nSe supero el limite de carga, el programa ha finalizado. Precio final: $"+ str(pre_total))