#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint
from collections import deque


def tipoBuque():
	numero = randint(1,100)
	if (numero >= 0) and (numero <= 40):
		return [4,3]
	elif (numero >40) and (numero <= 75):
		return [3,2]
	elif (numero > 75) and (numero <= 100):
		return [2,1]

def tiempoEntreLlegadas():
	dias = randint(1,100)
	if (dias >= 0) and (dias <= 20):
		return 1
	elif (dias > 20) and (dias <= 45):
		return 2
	elif (dias > 45) and (dias <= 80):
		return 3
	elif (dias > 80) and (dias <= 95):
		return 4
	elif (dias > 95) and (dias <= 100):
		return 5

def simulacion(tiempo):
	
	Aocupado = 1
	Bocupado = 1
	
	Adesocupado = 0
	Bdesocupado = 0

	totalBuques = 1
	diasEnPuerto = 0
	proximoBuque = 1

	colaBuque = deque([])

	nuevoBuque = tipoBuque()
	colaBuque.append(nuevoBuque)

	n = 0
	while n < tiempo:

		Aocupado -= 1
		Bocupado -= 1

		if (proximoBuque <= 0):
			
			nuevoBuque = tipoBuque()
			colaBuque.append(nuevoBuque)

			proximoBuque = tiempoEntreLlegadas()
			totalBuques += 1

		proximoBuque -= 1


		if (Aocupado <= 0):
			
			if (Aocupado<= -1):
				Adesocupado += 1
			if (len(colaBuque) > 0):
				siguiente = colaBuque.popleft()
				Aocupado = siguiente[0]
		else:
			diasEnPuerto += 1

		if (Bocupado <= 0):

			if (Bocupado<= -1):
				Bdesocupado += 1

			if (len(colaBuque) > 0):
				siguiente = colaBuque.popleft()
				Bocupado = siguiente[1]
		else:
			diasEnPuerto += 1



		n += 1
		
	return totalBuques, diasEnPuerto, Adesocupado, Bdesocupado

tiempo = int(input('Indique el numero de dias: '))

totalBuques, diasEnPuerto, Adesocupado, Bdesocupado = simulacion(tiempo)

print('Cantidad de buques: ', totalBuques)
print('Días en puerto: ', diasEnPuerto)
print('Días Puerto A desocupado: ', Adesocupado)
print('Días Puerto B desocupado: ', Bdesocupado)
print('Porcentaje de tiempo el puerto A esta desocupado:      '+str(Adesocupado*100/tiempo)+'%')
print('Porcentaje de tiempo el puerto B esta desocupado:      '+str(Bdesocupado*100/tiempo)+'%')
