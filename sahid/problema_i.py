#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint, uniform
from collections import deque
from math import modf, log, sqrt, fabs
import numpy as np

def generarClientes():
	cliente = np.random.exponential(1)
	cliente = round(cliente)
	return cliente

def clienteDeclina(longitud_cola):
	probabilidad = randint(1,100)
	if (6 <= longitud_cola) and (longitud_cola <= 8):
		if(0 <= probabilidad) and (probabilidad <= 20):
			return 1       
	if (9 <= longitud_cola) and (longitud_cola <= 10):
		if(0 <= probabilidad) and (probabilidad <= 40):
			return 1
	if (11 <= longitud_cola) and (longitud_cola <= 14):
		if(0 <= probabilidad) and (probabilidad <= 60):
			return 1
	if longitud_cola >= 15:
		if(0 <= probabilidad) and (probabilidad <= 80):
			return 1
	return 0

def tiempoServicio():
	tiempo = uniform(3,5)
	tiempo = round(tiempo)
	return tiempo


def simulacion(tiempo):
		
	Aocupado = 1
	Bocupado = 1
	Cocupado = 1
	Docupado = 1

	Adesocupado = 0
	Bdesocupado = 0
	Cdesocupado = 0
	Ddesocupado = 0

	proximos_cliente = 1
	
	tiempo_sistema = 0
	aceptan = 0
	declinan = 0

	cola = []

	n = 0
	total_clientes = 0

	while n < tiempo:

		if (len(cola)> 0):
			i = 0
			while (i < len(cola)):
				cola[i]+=1
				i+=1

		Aocupado -= 1
		Bocupado -= 1
		Cocupado -= 1
		Docupado -= 1
		
		cliente = 0
		clientes = generarClientes()

		clientes_sistema = 0
		while cliente < clientes:
			if clienteDeclina(len(cola)):
				declinan += 1
			else:
				cola.append(0)
				aceptan+=1

			cliente+=1

		if (Aocupado <= 0):


			if (Aocupado <= -1):
				Adesocupado+=1

			if (len(cola) > 0):
				espera = cola.pop()
				tiempo_servicio = tiempoServicio()
				Aocupado = tiempo_servicio
				tiempo_sistema+= tiempo_servicio + espera

		if (Bocupado <= 0):

			if (Bocupado <= -1):
				Bdesocupado+=1

			if (len(cola) > 0):
				espera = cola.pop()

				tiempo_servicio = tiempoServicio()
				Bocupado =tiempo_servicio
				tiempo_sistema+= tiempo_servicio + espera

		if (Cocupado <= 0):

			if (Cocupado <= -1):
				Cdesocupado+=1

			if (len(cola) > 0):
				espera = cola.pop()

				tiempo_servicio = tiempoServicio()
				Cocupado = tiempo_servicio
				tiempo_sistema+= tiempo_servicio + espera

		if (Docupado <= 0):

			if (Docupado <= -1):
				Ddesocupado+=1

			if (len(cola) > 0):
				espera = cola.pop()

				tiempo_servicio = tiempoServicio()
				Docupado = tiempo_servicio

				tiempo_sistema+= tiempo_servicio + espera


		n+=1
	total_clientes = aceptan + declinan
	tiempo_promedio_sistema = round(tiempo_sistema/aceptan)
	return total_clientes, declinan, tiempo_promedio_sistema,Adesocupado, Bdesocupado, Cdesocupado, Ddesocupado
	#return total_clientes


# Usando nivel de confianza 95% donde su respectivo coeficiente de confianza es -1,96
minutos=int(input('Indique la cantidad de minutos:'))  

totalClientes, totaldeclinan, tiempo_promedio_sistema, tiempoDesocupadoA, tiempoDesocupadoB, tiempoDesocupadoC, tiempoDesocupadoD = simulacion(minutos)

print("El total de clientes fueron: " + str(totalClientes))
print("El total de personas que declinaron fueron: " + str(totaldeclinan))
print("Tiempo esperado que pasa cliente en el sistema: " + str(tiempo_promedio_sistema)+" minutos")
print('Porcentaje de clientes que declinan acceder al servicio:   '+str(round(totaldeclinan*100/totalClientes))+'%')
print('Porcentaje de tiempo que la caja A esta desocupado:      '+str(tiempoDesocupadoA*100/minutos)+'%')
print('Porcentaje de tiempo que la caja B esta desocupado:      '+str(tiempoDesocupadoB*100/minutos)+'%')
print('Porcentaje de tiempo que la caja C esta desocupado:      '+str(tiempoDesocupadoC*100/minutos)+'%')
print('Porcentaje de tiempo que la caja D esta desocupado:      '+str(tiempoDesocupadoD*100/minutos)+'%')


