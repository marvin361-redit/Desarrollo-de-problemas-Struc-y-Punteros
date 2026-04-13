# ejercicio4.py
# En una lista clasificar los numeros primos y compuestos
# Materia: Estructura de Datos
# Tema: Struct y Punteros en Python

# no necesito importar nada para este ejercicio

# creo mi lista de numeros para clasificar
mi_lista = list(range(2, 51))  # del 2 al 50

# funcion para saber si un numero es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # encontre un divisor, no es primo
    return True  # no tiene divisores, es primo

# clasifico los numeros
primos = []
compuestos = []

for numero in mi_lista:
    if es_primo(numero):
        primos.append(numero)
    else:
        compuestos.append(numero)

print("Lista original:", mi_lista)
print()
print("Numeros PRIMOS (" + str(len(primos)) + "):")
print(primos)
print()
print("Numeros COMPUESTOS (" + str(len(compuestos)) + "):")
print(compuestos)

# -----------------------------------------------------------
# CONCEPTO DE PUNTERO (referencia en Python)
# uso el operador IS para verificar si dos variables
# apuntan al mismo objeto en memoria
# -----------------------------------------------------------
lista_ref = primos       # referencia al mismo objeto
lista_copia = primos[:]  # copia nueva, objeto diferente

print()
print("-- Verificacion con operador IS --")
print("lista_ref is primos:   ", lista_ref is primos)    # True
print("lista_copia is primos: ", lista_copia is primos)  # False
print()
print("id de primos:     ", id(primos))
print("id de lista_ref:  ", id(lista_ref))
print("id de lista_copia:", id(lista_copia))