#! /usr/bin/python
# -*- encoding: utf-8 -*-

from random import randint, uniform
from collections import deque
from math import log, sqrt, fabs

def generarTiempoReparacion():
    x = randint(1,100)*1.0/100.0
    if x == 1.0:
        x = 0.99
    tiempo = - (log(1-x))/2
    return round(tiempo)
    
def generarTiempoFallo():
    x = randint(1,100)*1.0/100.0
    if x == 1.0:
        x = 0.99
    falla = - log(1-x)
    return round(falla)

def simulacion(n,s):

	colaTrabajo = []
	colaRepuesto = []
	colaReparacion = []

	falloSistema = False
	tiempo = 0

	for i in range(0,n):
		colaTrabajo.append(generarTiempoFallo())
	for j in range(0,s):
		colaRepuesto.append(generarTiempoFallo())

	esta_reparando = False
	reparacion = 0
	

	while not falloSistema:

		for i in colaTrabajo:
			if i <= tiempo:
				if len(colaRepuesto) > 0:
					colaTrabajo.remove(i)
					colaReparacion.append(generarTiempoReparacion())
					colaTrabajo.append(tiempo + colaRepuesto.pop(0))
				elif len(colaRepuesto) <= 0:
					falloSistema = True
					return tiempo

	
		if (reparacion <= 0 and not esta_reparando):
			if (len(colaReparacion) > 0):
				reparacion = colaReparacion.pop(0)
				esta_reparando = True
		elif (reparacion <= 0 and esta_reparando):
			colaRepuesto.append(generarTiempoFallo())
			esta_reparando = False
			if (len(colaReparacion) > 0):
				reparacion = colaReparacion.pop(0)
				esta_reparando = True

		reparacion -=1
		tiempo +=1

n = int(input('introduzca numero de maquinas: '))
s = int(input('introduzca numero de maquinas de repuesto: '))
r = int(input('introduzca numero de repeticiones: '))

t = 0
i = 0
while i < r:
	t += simulacion(n,s)
	i+=1

print('el tiempo esperado es: ', t/r)
