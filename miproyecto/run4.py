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

# valor promedio de cada ciclo == valPromCiclo <- 1200
valPromCiclo = int(1200)

# recolección de los datos del estudiante: edad y modalidad
print("_____Datos del estudiante_____")
modalidad = input("Modalidad en que se encuentra: ")
edad = int(input("Edad: "))

# uso de condicionales para asignar costo y ciclos
# costo para edad
if edad <= 20:
	valPromSeg = int(100)
else:
	valPromSeg = int(150)

# número de ciclos según modalidad
if modalidad == "Distancia":
	nCiclos = int(10)
else:
	nCiclos = int(8)

# cálculo del costo
total = float((valPromCiclo*nCiclos)+(valPromSeg*nCiclos))

# salida
print("%s = $%.2f" % ("Costo total de la carrera universitaria", total))