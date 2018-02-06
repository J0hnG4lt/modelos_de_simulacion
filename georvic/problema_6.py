#!/usr/bin/env python3

"""
Sahid Reyes 10-10603
Georvic Tur 12-11402
"""

from scipy.stats import poisson
import numpy as np
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import choice
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import normalize

def tiempo_recorrido(numero_pasajeros) :
    return 100 * ( 1 + 0.1 * np.log(numero_pasajeros) )

def tiempo_desembarque(numero_pasajeros_desembarque, numero_pasajeros_embarque) :
    return 20 * ( 1 + 0.1 * np.log(numero_pasajeros_desembarque + numero_pasajeros_embarque) )

# Leemos la distribución empírica de nemb
with open("distribucion_nemb_problema_6.txt") as f :
    lineas = f.read().splitlines()

distribucion_nemb = list(map(int, lineas))

# Hacemos un ajuste  de una función normal sobre la data
mu, std = norm.fit(distribucion_nemb)

#plt.hist(distribucion_nemb, bins='auto')  # arguments are passed to np.histogram
#plt.title("Histograma con la distribución empírica de nemb")
#plt.show()


    
def generar_numero_de_embarcados() :
    
    return np.random.normal(mu, std)
    

def generar_numero_de_estaciones(estacion_de_entrada) :
    # Las estaciones van del 1 al 10
    numero_de_estaciones_a_la_derecha = 10-estacion_de_entrada
    numero_de_estaciones_por_recorrer = np.random.binomial(numero_de_estaciones_a_la_derecha, 0.5)
    return numero_de_estaciones_por_recorrer

class Pasajero :
    
    def __init__(self) :
        self.id = 0
        self.estacion_embarque = None
        self.estacion_desembarque = None

class Estacion :
    
    def __init__(self) :
        self.pasajeros_embarcados = []
        self.pasajeros_desembarcados = []
        self.tiempo_llegada = 0.0
        self.tiempo_salida = 0.0

estaciones = [Estacion() for i in range(10)]
pasajeros = []

tiempo = 0.0
nemb = 0
ndesemb = 0
numero_pasajeros = 0
numero_pasajeros_por_estacion = []

for estacion in range(10) :
    
    estaciones[estacion].tiempo_llegada = tiempo
    
    # Genero nuevos pasajeros
    nemb = int(generar_numero_de_embarcados())
    
    numero_pasajeros += nemb
    
    for pasajero in range(nemb) :
        n_pasajero = Pasajero()
        n_pasajero.id = len(pasajeros)
        n_pasajero.estacion_embarque = estacion
        n_pasajero.estacion_desembarque = generar_numero_de_estaciones(estacion+1)+estacion
        pasajeros.append(n_pasajero)
        estaciones[estacion].pasajeros_embarcados.append(n_pasajero)
    
    # Determino quiénes salen de la estación
    i = 0
    while (i < len(pasajeros)) :
        pasajero = pasajeros[i]
        if pasajero.estacion_desembarque == estacion :
            estaciones[estacion].pasajeros_desembarcados.append(pasajero)
            pasajeros.pop(i)
            numero_pasajeros -= 1
        i += 1
    
    print(estacion,nemb, len(estaciones[estacion].pasajeros_desembarcados))
    tiempo += tiempo_desembarque(nemb, len(estaciones[estacion].pasajeros_desembarcados))
    estaciones[estacion].tiempo_salida = tiempo
    
    tiempo += tiempo_recorrido(numero_pasajeros)
    
    numero_pasajeros_por_estacion.append(numero_pasajeros)
    
print("El tiempo total de reccorido es (segundos): ", tiempo)
print("El número de pasajeros promedio por estación: ", np.mean(numero_pasajeros_por_estacion))
print("El número máximo de pasajeros embarcados: ", max([len(x.pasajeros_embarcados) for x in estaciones]))

