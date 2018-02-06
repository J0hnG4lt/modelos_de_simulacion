#!/usr/bin/env python3

"""
Sahid Reyes 10-10603
Georvic Tur 12-11402
"""

from scipy.stats import poisson
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import choice

import numpy as np

# (Clientes por hora)*(factor de conversión a minuto)
mu = 60*(60)

# Intervalo de tiempo de servicio en minutos
tiempos_servicio = [3,5]

def decline(queue_length) :
    
    if queue_length <= 5 :
        return 0.0
    elif 6 <= queue_length <= 8 :
        return 0.2
    elif 8 <= queue_length <= 10 :
        return 0.4
    elif 11 <= queue_length <= 14 :
        return 0.6
    elif 15 <= queue_length :
        return 0.8



# Se calculan las llegadas pues son independientes de la atención

horas = 0
llegadas = []
max_horas = 8*(1/60) # en minutos
tiempo_de_llegada = 0

while (horas < max_horas) :
    
    # Llega un cliente
    tiempo_de_llegada = exponential(scale = (1/mu))
    #print(tiempo_de_llegada)
    
    horas += tiempo_de_llegada
    
    llegadas.append(horas)



class Cajero :
    
    def __init__(self) :
        
        self.inicio = 0.0
        self.tiempo_de_atencion = 0.0
        self.disponible = True
        self.tiempo_desocupado = 0.0

class Cliente :
    
    def __init__(self) :
        
        self.numero_de_cliente = 0
        self.tiempo_de_espera = 0.0
        self.tiempo_de_llegada = 0.0
        self.tiempo_de_salida = 0.0
     
cajeros = [Cajero() for i in range(4)]
clientes = []
for numero, llegada in enumerate(llegadas) :
    cliente_obj = Cliente()
    cliente_obj.tiempo_de_llegada = llegada
    cliente_obj.numero_de_cliente = numero
    clientes.append(cliente_obj)

step = 0.1
horas = 0
max_horas_2 = 8*60 # en minutos
cliente = 0
clientes_que_se_quedan = 0
tiempo_por_cliente = [0.0 for i in llegadas]
cola_clientes = 0
cajeros_disponible = [True for i in range(4)]
cajeros_espera = [0.0 for i in range(4)]
cliente_atendido = 0

while (horas < max_horas_2) :
    
    # Llega un cliente
    if (cliente < len(llegadas)) and (llegadas[cliente] <= horas) :
        
        # Determinamos si el cliente declina al ver la cola
        cliente_actual_declina = choice([True, False],p = [decline(cola_clientes), 1-decline(cola_clientes)])
        
        # Si no declina, lo ponemos en la cola
        if not cliente_actual_declina :
            cola_clientes += 1
            clientes_que_se_quedan += 1
            print("LLegada de cliente. Cola clientes: ", cola_clientes, "tiempo (minutos): ", horas)
        else :
            print("Declina")
            
        cliente += 1
    
    
    # Encontramos un cajero disponible
    for i in range(4) :
        if (cola_clientes > 0) and cajeros[i].disponible :
            cajeros[i].disponible = False
            cajeros[i].inicio = horas
            cajeros[i].tiempo_de_atencion = uniform(low=tiempos_servicio[0],
                                                    high=tiempos_servicio[1])
            
            cola_clientes -= 1
            print("Salida de cliente. Cola clientes: ", cola_clientes, "tiempo (minutos) : ", horas, "Cajero: ", i)
            
            # determinar si esto va aquí
            break
    
    # determinamos si los cajeros se desocuparon
    for i in range(4) :
        if (not cajeros[i].disponible) and ((cajeros[i].inicio + cajeros[i].tiempo_de_atencion) <= horas) :
            cajeros[i].disponible = True
            print("Se desocupa Cajero: ", i)
            clientes[cliente_atendido].tiempo_de_salida = horas
            clientes[cliente_atendido].tiempo_de_espera = horas - clientes[cliente_atendido].tiempo_de_llegada
            cliente_atendido += 1
        
        if cajeros[i].disponible :
            cajeros[i].tiempo_desocupado += step
        
    horas += step

# determinamos los tiempos de espera
tiempos_de_espera = []
for cliente in clientes :
    tiempos_de_espera.append(cliente.tiempo_de_espera)

print()
print()
print("Tiempo de espera promedio de un cliente (minutos): ", np.mean(tiempos_de_espera))
print("Porcentaje de clientes que declinan: ", ((len(llegadas)-clientes_que_se_quedan)/len(llegadas))*100)
for i in range(4) :
    print("Porcentaje de tiempo desocupado del cajero {}: {}".format(i, (cajeros[i].tiempo_desocupado/horas)*100))
