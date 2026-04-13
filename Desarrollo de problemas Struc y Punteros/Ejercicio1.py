# ejercicio1.py
# Crear una matriz 5x4 con numeros aleatorios
# Materia: Estructura de Datos
# Tema: Struct y Punteros en Python

import random  # necesito esta libreria para generar numeros aleatorios

# creo la matriz vacia de 5 filas y 4 columnas
matriz = []

for i in range(5):
    fila = []
    for j in range(4):
        numero = random.randint(1, 100)  # numero aleatorio entre 1 y 100
        fila.append(numero)
    matriz.append(fila)

# muestro la matriz
print("Matriz 5x4 con numeros aleatorios:")
print()
for fila in matriz:
    print(fila)

# -----------------------------------------------------------
# CONCEPTO DE PUNTERO (referencia en Python)
# en Python cuando hago  otra_variable = matriz
# las dos variables apuntan al mismo objeto en memoria
# es como un puntero en C
# -----------------------------------------------------------
otra_variable = matriz

print()
print("-- Concepto de referencia (puntero) --")
print("otra_variable is matriz:", otra_variable is matriz)  # True = mismo objeto
print("id de matriz:         ", id(matriz))
print("id de otra_variable:  ", id(otra_variable))