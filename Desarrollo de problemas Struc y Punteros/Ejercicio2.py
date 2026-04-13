# ejercicio2.py
# Crear una lista con numeros desde 505 hasta 615
# Materia: Estructura de Datos
# Tema: Struct y Punteros en Python

# no necesito importar nada para este ejercicio
# range() ya viene incluido en Python

# creo la lista con range, el +1 es para que incluya el 615
mi_lista = list(range(505, 616))

print("Lista de numeros del 505 al 615:")
print(mi_lista)
print()
print("Cantidad de elementos:", len(mi_lista))

# -----------------------------------------------------------
# CONCEPTO DE PUNTERO (referencia en Python)
# si dentro de una funcion solo reasigno la variable,
# el objeto original NO se modifica
# esto es diferente a modificarlo directamente
# -----------------------------------------------------------

def intentar_cambiar(lista):
    lista = [1, 2, 3]  # esto solo cambia la variable local, no el original
    print("Dentro de la funcion:", lista)

print()
print("-- Concepto de referencia (puntero) --")
print("Lista antes de llamar la funcion:", mi_lista[:5], "...")
intentar_cambiar(mi_lista)
print("Lista despues de llamar la funcion:", mi_lista[:5], "...")
print("El objeto original NO cambio porque solo reasigne la referencia local")