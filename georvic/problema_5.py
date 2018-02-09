#!/usr/bin/env python3

from scipy.stats import poisson
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import choice

import numpy as np


def generar_tiempos_de_llegada() :
    
    return choice([1,2,3,4,5], p = [0.2,0.25,0.35,0.15,0.05])

def generar_tipo_de_buque() :

    return choice(["tanque", "mediano", "pequeño"], p = [0.4,0.35,0.25])

def tiempo_atencion(tipo_buque, tipo_terminal) :
    if tipo_buque == "tanque" :
        if tipo_terminal == "A":
            return 4
        elif tipo_terminal == "B" :
            return 3
    elif tipo_buque == "mediano" :
        if tipo_terminal == "A":
            return 3
        elif tipo_terminal == "B" :
            return 2
    elif tipo_buque == "pequeño":
        if tipo_terminal == "A":
            return 2
        elif tipo_terminal == "B" :
            return 1

class Buque :
    
    def __init__(self) :
        
        self.tipo = None
        self.tiempo_llegada = None
        self.tiempo_salida = None

class Terminal :
    
    def __init__(self) :
        
        self.buques = []
        self.tiempo_desocupado = 0
        self.ocupado = False

A = Terminal()
B = Terminal()

# Genero los eventos de llegada

dias_max = 200
tiempo = 0 # en días
cola = []

while tiempo < dias_max :
    
    llegada = generar_tiempos_de_llegada()
    
    tiempo += llegada
    
    buque = Buque()
    buque.tipo = generar_tipo_de_buque()
    buque.tiempo_llegada = tiempo
    
    cola.append(buque)
    
tiempo = 0
puerto = []

total_buques = len(cola)

numero_buques_en_puerto = []
numero_buques_tanque_en_puerto = []
numero_buques_medianos_en_puerto = []
numero_buques_pequenos_en_puerto = []

while tiempo < dias_max :
    
    print(puerto)
    
    # Llega un buque
    if cola[0].tiempo_llegada <= tiempo :
        
        buque = cola.pop(0)
        puerto.append(buque)
        
    
    if len(puerto) > 0 :
        
        # atiendo a un buque
        
        if not A.ocupado :
            
            buque_atendido = puerto.pop(0)
            buque_atendido.tiempo_salida = buque_atendido.tiempo_llegada + tiempo_atencion(buque_atendido.tipo, "A")
            A.buques.append(buque_atendido)
            A.ocupado = True
        
        elif not B.ocupado :
            
            buque_atendido = puerto.pop(0)
            buque_atendido.tiempo_salida = buque_atendido.tiempo_llegada + tiempo_atencion(buque_atendido.tipo, "B")
            B.buques.append(buque_atendido)
            B.ocupado = True
    
    # determino si ya un buque fue atendido
    
    if A.ocupado :
        
        if A.buques[-1].tiempo_salida <= tiempo :
            A.ocupado = False
    
    else :
        A.tiempo_desocupado += 1
    
    if B.ocupado :
        
        if B.buques[-1].tiempo_salida <= tiempo :
            B.ocupado = False
    
    else :
        B.tiempo_desocupado += 1
    
    numero_buques_tanque_en_puerto.append(len([navio for navio in puerto if navio.tipo == "tanque"]))
    numero_buques_medianos_en_puerto.append(len([navio for navio in puerto if navio.tipo == "mediano"]))
    numero_buques_pequenos_en_puerto.append(len([navio for navio in puerto if navio.tipo == "pequeño"]))
    numero_buques_en_puerto.append(len(puerto))
       
    
    tiempo += 1

numero_dias_buques_en_puerto = []
numero_dias_buques_tanque_en_puerto = []
numero_dias_buques_medianos_en_puerto = []
numero_dias_buques_pequenos_en_puerto = []

for buque in A.buques :
    
    duracion = buque.tiempo_salida - buque.tiempo_llegada
    
    numero_dias_buques_en_puerto.append(duracion)
    
    if buque.tipo == "tanque" :
        numero_dias_buques_tanque_en_puerto.append(duracion)
    elif buque.tipo == "pequeño" :
        numero_dias_buques_pequenos_en_puerto.append(duracion)
    elif buque.tipo == "mediano" :
        numero_dias_buques_medianos_en_puerto.append(duracion)

print("promedio de buques por día en puerto: {}".format(np.mean(numero_buques_en_puerto)))
print("promedio de buques tanque por día en puerto: {}".format(np.mean(numero_buques_tanque_en_puerto)))
print("promedio de buques medianos por día en puerto: {}".format(np.mean(numero_buques_medianos_en_puerto)))
print("promedio de buques pequeños por día en puerto: {}".format(np.mean(numero_buques_pequenos_en_puerto)))
print("promedio de días en puerto de buques tanque por día en puerto: {}".format(np.mean(numero_dias_buques_tanque_en_puerto)))
print("promedio de días en puerto de buques medianos por día en puerto: {}".format(np.mean(numero_dias_buques_medianos_en_puerto)))
print("promedio de días en puerto de buques pequeños por día en puerto: {}".format(np.mean(numero_dias_buques_pequenos_en_puerto)))
print("Tiempo desocupado del terminal A: {}".format(A.tiempo_desocupado))
print("Tiempo desocupado del terminal B: {}".format(B.tiempo_desocupado))
print("Días totales: {}".format(dias_max))
print("total de buques: {}".format(total_buques))
print("")

