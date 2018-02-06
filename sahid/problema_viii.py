#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint
from math import modf, log, sqrt, fabs

# Funcion que genera la comision a pagar por vender un carro mediano
def generarMediano():
	probabilidad = randint(1,100)
	if (probabilidad >= 0) and (probabilidad <= 40):
		comision = 400
	elif (probabilidad > 40) and (probabilidad <= 100):
		comision = 500
	return comision

# Funcion que genera la comision a pagar por vender un carro mediano
def generarLujo():
	probabilidad = randint(1,100)
	if (probabilidad >= 0) and (probabilidad <= 35):
		comision = 1000
	elif (probabilidad > 35) and (probabilidad <= 75):
		comision = 1500
	elif (probabilidad > 75) and (probabilidad <= 100):
		comision = 2000
	return comision

def generarAuto(cantidad):
	total = 0
	i = 0
	while i < cantidad:
		probabilidad = randint(1,100)
		if (probabilidad >= 0) and (probabilidad <= 40):
			acumulado = 250
		if (probabilidad > 40) and (probabilidad <= 75):
			acumulado = generarMediano()
		if (probabilidad > 75) and (probabilidad <= 100):
			acumulado = generarLujo()
		total += acumulado
		i+=1
	return total


def simulacion():
	i = 0
	acumulado = 0
	comision  = 0
	while i < 5:
		probabilidad_vendidos = randint(1,100)
		if (probabilidad_vendidos >= 0) and (probabilidad_vendidos <= 10):
			comision = 0
		elif (probabilidad_vendidos > 10) and (probabilidad_vendidos <= 25):
			comision = generarAuto(1)
		elif (probabilidad_vendidos > 25) and (probabilidad_vendidos <= 45):
			comision = generarAuto(2)
		elif (probabilidad_vendidos > 45) and (probabilidad_vendidos <= 70):
			comision = generarAuto(3)
		elif (probabilidad_vendidos > 75) and (probabilidad_vendidos <= 90):
			comision = generarAuto(4)
		elif (probabilidad_vendidos > 90) and (probabilidad_vendidos <= 100):
			comision = generarAuto(5)
		acumulado += comision
		i += 1
	total = acumulado/5
	return total

repeticiones = int(input("Cantidad de veces a simular: "))

i = 0
comision = 0
while i < repeticiones:
	comision += simulacion()
	i+=1

promedio = comision/repeticiones
print('La comisión promedio es: '+str(promedio))