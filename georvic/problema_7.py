#!/usr/bin/env python3



from scipy.stats import poisson
import numpy as np
from numpy.random import uniform
from numpy.random import exponential
from numpy.random import choice
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.preprocessing import normalize


def generar_demanda_diaria() :
    
    return choice([12,13,14,15,16,17],
                  p = [0.05,0.15,0.25,0.35,0.15,0.05])
                  
def generar_tiempo_entrega() :
    
    return choice([1,2,3,4],
                  p = [0.2,0.3,0.35,0.15])

R = 20
Q = 100

# $ / (producto * día)
costo_inventario = 0.2

# $ / (producto * día)
costo_escasez = 1

# $ / pedido
costo_pedido = 10




tiempo_max = 1000
paso = 1

for R in range(Q) :
    
    tiempo = 0
    escasez = 0
    # guarda los tiempos
    por_entregar = []
    # E(costo_total_inventario) + E(costo_total_pedidos) + E(costo_total_escasez)
    costo_total = 0

    productos_en_almacen = Q

    while tiempo < tiempo_max :
        
        demanda = generar_demanda_diaria()
        
        # Si los productos en almacen no cubren la demanda
        if productos_en_almacen < demanda :
            productos_en_almacen = 0
            
            # la escasez se acumula
            escasez = escasez + demanda - productos_en_almacen
        else :
            productos_en_almacen -= demanda
        
        
        # Si se alcanza el punto de reorden
        hay_pedido = 0
        if productos_en_almacen <= R :
            tiempo_de_entrega = generar_tiempo_entrega()
            hay_pedido = 1
            por_entregar = por_entregar + ( [tiempo_de_entrega] * Q )
        
        # Si la entrega llega
        entrega = len(list(filter(lambda x : x <= 0, por_entregar)))
        por_entrega = list(filter(lambda x : x > 0, por_entregar))
        
        productos_en_almacen += entrega
        
        costo_total = productos_en_almacen*costo_inventario + escasez*costo_escasez + hay_pedido*costo_pedido
        
        tiempo += paso

    print("El costo total para R={} es: {} $".format(R,costo_total))
