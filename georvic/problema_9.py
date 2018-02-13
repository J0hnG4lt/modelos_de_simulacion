#!/usr/bin/env python3

"""
Sahid Reyes 10-10603
Georvic Tur 12-11402
"""

from scipy.stats import poisson
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import choice
import math

import numpy as np

from scipy.integrate import quad

mu = 5 / 60 # en minutos

cola_de_a = []
cola_de_b = []

def distribucion_tiempo_procesamiento(x) :
    
    if 1 <= x <= 3 :
        return (x-1)/4
    elif 3 <= x <= 5 :
        return (5-x)/5
    

def distribucion_acumulada_tiempo_procesamiento(x) :
    #return quad(distribucion_tiempo_procesamiento, 1,x)
    
    # Luego de integrar
    if 1 <= x <= 3 :
        return (x**2)/8 - x/4 + (1/8)
    elif 3 <= x <= 5 :
        return -17/8 + (5/4)*x - (x**2)/8

def generar_tiempo_procesamiento() :
    
    aleatorio = uniform(low = 1, high = 5)
    if aleatorio < 3 :
        b = 1/4
        a = 1/8
        c = (1/8) - aleatorio
    elif aleatorio >= 3 :
        b = 5/4
        a = 1/8
        c = (-17/8) - aleatorio
        
    d = b**2-4*a*c
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d)) / (2 * a)
    
    return x, y


class Trabajo :
    
    def __init__(self) :
        self.llegada = None
        self.tiempo_procesamiento_a = None
        self.tiempo_procesamiento_b = None
        self.fin = None

max_tiempo = 1000
tiempo = 0
paso = 1
llegadas = []
tiempo_llegadas_acumulado = 0

while tiempo < max_tiempo :

    tiempo_de_llegada = exponential(scale = (1/mu))
    tiempo_llegadas_acumulado += tiempo_de_llegada
    trabajo = Trabajo()
    trabajo.llegada = tiempo_llegadas_acumulado
    llegadas.append(trabajo)
    
    tiempo += paso
    

tiempo = 0
numero_de_trabajos_en_taller = []
tiempo_parado_a = 0
terminados = []

while tiempo < max_tiempo :
    
    # Si llega un trabajo en A
    if len(llegadas) > 0 and llegadas[0].llegada <= tiempo :
        trabajo = llegadas.pop(0)
        trabajo.tiempo_procesamiento_a = uniform(low=6, high=10)
        cola_de_a.append(trabajo)
    
    # si un trabajo se puede pasar de A a B
    if len(cola_de_a) > 0 and cola_de_a[0].tiempo_procesamiento_a <= 0 and len(cola_de_b) < 4 :
        trabajo = cola_de_a.pop(0)
        trabajo.tiempo_procesamiento_b = uniform(low=6, high=10)
        cola_de_b.append(trabajo)
        
    elif len(cola_de_a) > 0 and cola_de_a[0].tiempo_procesamiento_a > 0 and len(cola_de_b) < 4  :
        cola_de_a[0].tiempo_procesamiento_a -= paso
    
    elif len(cola_de_a) > 0 and cola_de_a[0].tiempo_procesamiento_a <= 0 and len(cola_de_b) >= 4  :
        tiempo_parado_a += paso
    
    # Si un trabajo se puede sacar de b
    if len(cola_de_b) > 0 and cola_de_b[0].tiempo_procesamiento_b <= 0  :
        trabajo = cola_de_b.pop(0)
        trabajo.fin = tiempo
        terminados.append(trabajo)
    elif len(cola_de_b) > 0 and cola_de_b[0].tiempo_procesamiento_b > 0 :
        cola_de_b[0].tiempo_procesamiento_b -= paso
    
    numero_de_trabajos_en_taller.append(len(cola_de_a) + len(cola_de_b))
        
    tiempo += paso

print("Número promedio de trabajos en taller: {}".format(np.mean(numero_de_trabajos_en_taller)))
print("Tiempo en que A estuvo parado: {}".format(tiempo_parado_a))
print("Tiempo promedio de procesamiento de un trabajo: {}".format(np.mean([(trabajo.fin-trabajo.llegada) for trabajo in terminados])))
