#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint, uniform
from collections import deque
from math import modf, log, sqrt, fabs
import numpy as np

def generarTiempoA():
    tiempo = uniform(6,10)
    tiempo = round(tiempo)
    return tiempo

def generarTiempoB():
    x = randint(1,100)*1.0/100.0
    if x == 1.0:
        x = 0.99
    if x < 0.5:
        tiempoB = 1+sqrt(8*x)
    if x >= 0.5:
        tiempoB = 5-sqrt(8-8*x)
    return tiempoB

def generarTrabajos(m):
    x = randint(1,10000000)*1.0/10000000.0
    if x == 1.0:
        x = 0.99
    trabajos = -(log(1-x))*m/60
    trabajos += 0.1
    trabajos = round(trabajos)
    return 5

def simulacion(tiempo_max):

    colaA = []
    colaB = []
    tiempo_fallo = 0
    terminacionA = 0
    terminacionB = 0
    tiempo_terminacion = 0
    terminados = 0
    tiempo = 0

    A_ocupado = 0
    B_ocupado = 0
    A_trabajando = False
    B_trabajando = False
    cantidad_trabajos = 0

    while tiempo < tiempo_max:
    
        trabajos = generarTrabajos(tiempo_max)

        for i in range(0,trabajos):
            colaA.append(0)

        cantidad_trabajos += trabajos
        print("trabajos: ",trabajos)
        print("acumulados: ",cantidad_trabajos)

        A_ocupado-=1
        B_ocupado-=1


        if (A_ocupado <= 0 and not A_trabajando):
            if (len(colaA) > 0):
                esperaA = colaA.pop(0)
                A_ocupado = generarTiempoA()
                A_trabajando = True
                terminacionA = esperaA + A_ocupado

        if (A_ocupado <= 0 and A_trabajando):
            if (len(colaB) < 4):
                colaB.append(0)
                A_trabajando = False
            else:
                tiempo_fallo +=1
                if (A_ocupado > 0):
                    if (len(colaA) > 0):
                        i = 0
                        while (i < len(colaA)):
                            colaA[i]+=1
                            i+=1
        if (A_ocupado > 0):
            if (len(colaA) > 0):
                i = 0
                while (i < len(colaA)):
                    colaA[i]+=1
                    i+=1


        if (B_ocupado <= 0 and not B_trabajando):
            if (len(colaB) > 0):
                esperaB = colaB.pop(0)
                B_ocupado = generarTiempoB()
                B_trabajando = True
                terminacionB = esperaB + B_ocupado
        elif (B_ocupado <= 0 and B_trabajando):
            terminados +=1
            B_trabajando = False

        if (B_ocupado > 0):
            if (len(colaB) > 0):
                i = 0
                while (i < len(colaB)):
                    colaB[i]+=1
                    i+=1

        tiempo_terminacion += terminacionA + terminacionB
        tiempo += 1

    promedio_terminacion = tiempo_terminacion/tiempo_max

    return cantidad_trabajos, tiempo_fallo, promedio_terminacion, terminados

tiempo_max = int(input('introduzca la cantidad de minutos: '))
cantidad_trabajos, tiempo_fallo, promedio_terminacion, terminados = simulacion(tiempo_max)

print('El número esperado de trabajos en el taller: ',cantidad_trabajos)
print('El porcentaje de tiempo que se para el centro A: '+ str(tiempo_fallo*100/tiempo_max) + '%')
print('El tiempo esperado de terminación de un trabajo: ',promedio_terminacion)
print('Trabajos terminados: ',terminados)