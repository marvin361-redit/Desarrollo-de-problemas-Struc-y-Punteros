# ejercicio3.py
# Crear una tupla y elegir sus elementos
# Materia: Estructura de Datos
# Tema: Struct y Punteros en Python

# no necesito importar nada

# elegi estos elementos: datos de un estudiante
mi_tupla = ("Juan Perez", 20, "Ingenieria en Sistemas", 3.75, True)

print("Mi tupla:")
print(mi_tupla)
print()
print("Elemento 0 (nombre)  :", mi_tupla[0])
print("Elemento 1 (edad)    :", mi_tupla[1])
print("Elemento 2 (carrera) :", mi_tupla[2])
print("Elemento 3 (promedio):", mi_tupla[3])
print("Elemento 4 (activo)  :", mi_tupla[4])

# -----------------------------------------------------------
# CONCEPTO DE PUNTERO (referencia en Python)
# las tuplas son INMUTABLES, es como un const struct en C
# dos variables pueden apuntar a la misma tupla (mismo objeto)
# pero ninguna puede modificarla
# -----------------------------------------------------------
a = mi_tupla
b = a  # b apunta al mismo objeto que a

print()
print("-- Concepto de referencia (puntero) --")
print("a is b:", a is b)            # True = apuntan al mismo objeto
print("a is mi_tupla:", a is mi_tupla)  # True tambien

# si intento modificar la tupla, Python lanza un error
# mi_tupla[0] = "otro nombre"  <-- esto daria TypeError
print()
print("Las tuplas son inmutables (como const struct en C)")
print("No se pueden modificar una vez creadas")