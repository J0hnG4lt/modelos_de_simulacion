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

def generar_numero_automoviles_vendidos() :
    
    return choice([0,1,2,3,4,5], p = [0.1,0.15,0.2,0.25,0.2,0.1])


def generar_tipo_auto_vendido() :
    
    return choice(["compacto", "mediano", "lujo"], p = [0.4, 0.35, 0.25])

def generar_pago(tipo_auto) :
    
    if tipo_auto == "compacto" :
        return 250
    elif tipo_auto == "mediano" :
        return choice([400, 500], p = [0.4, 0.6])
    elif tipo_auto == "lujo" :
        return choice([1000, 1500, 2000], p = [0.35, 0.4, 0.25])

semanas = 50
vendedores = 5

semanas = int(input("Número de semanas: "))

ventas_por_semana = []
total_ganancias = [0.0 for x in range(semanas)]
promedio_vendedores_por_semana = []

# Por cada semana
for semana in range(semanas) :
    
    ventas_por_vendedor = [ [] for i in range(vendedores) ]
    
    ganancias_vendedor = [0.0 for x in range(vendedores)]
    
    # y cada vendedor
    for vendedor in range(vendedores) :
        
        # genero el número de ventas
        autos_vendidos = generar_numero_automoviles_vendidos()
        
        # y determino por cada venta el tipo de carro vendido
        for carro in range(autos_vendidos) :
            
            tipo = generar_tipo_auto_vendido()
            
            # y determino la comision ganada por dicha venta
            comision = generar_pago(tipo)
            
            ventas_por_vendedor[vendedor].append(comision)
            total_ganancias[semana] += comision
            ganancias_vendedor[vendedor] += comision
    
    promedio_vendedores_por_semana.append(np.mean(ganancias_vendedor))      
    ventas_por_semana.append(ventas_por_vendedor)

    
print("Ganancias promedio por vendedor por semana: ", np.mean(promedio_vendedores_por_semana))
