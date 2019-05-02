"""
	file: run4.py
	autor: @vysery98

	Deseamos obtener el costo de una carrera universitaria. El
	valor promedio de cada ciclo es de $1200, el valor promedio
	del seguro educativo (de cada ciclo) es de $100 si la edad 
	del estudiante es menor o igual a 20, caso contrario será 
	de $150. Si el estudiante tiene una modalidad a distancia,
	el número de ciclos a seguir es de 10, caso contrario deberá
	seguir 8 ciclos. Obtener la proyección del costo de la 
	carrera del estudiante.
"""

# declaración de variables
valPromCiclo = 1200
valPromCiclo = int(valPromCiclo)

# recolección de los datos del estudiante: edad y modalidad
print("_____Datos del estudiante_____")
modalidad = input("Modalidad en que se encuentra: ")
edad = input("Edad: ")
edad = int(edad)

# uso de condicionales

# costo para edad
if edad <= 20:
	valPromSeg = 100
	valPromSeg = int(valPromSeg)
else:
	valPromSeg = 150
	valPromSeg = int(valPromSeg)

# número de ciclos según modalidad
if modalidad == "Distancia":
	nCiclos = 10
	nCiclos = int(nCiclos)
else:
	nCiclos = 8
	nCiclos = int(nCiclos)

# cálculo del costo
total = ((valPromCiclo*nCiclos)+(valPromSeg*nCiclos))

# salida
print("%s = %d" % ("Costo total de la carrera universitaria", int(total)))