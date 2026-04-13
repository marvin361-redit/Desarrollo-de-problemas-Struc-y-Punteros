# ejercicio5.py
# Multiplicar dos valores de 7 digitos y expresar el resultado en texto
# Materia: Estructura de Datos
# Tema: Struct y Punteros en Python

import ctypes  # esta libreria me permite trabajar con memoria de bajo nivel (como C)

# mis dos numeros de 7 digitos
valor_a = 1234567
valor_b = 7654321

resultado = valor_a * valor_b

print("Multiplicacion de dos valores de 7 digitos:")
print(f"{valor_a} x {valor_b} = {resultado}")
print()

# funcion para convertir numero a texto en espanol
def numero_a_texto(n):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis",
                "siete", "ocho", "nueve", "diez", "once", "doce",
                "trece", "catorce", "quince", "dieciseis", "diecisiete",
                "dieciocho", "diecinueve"]
    decenas  = ["", "", "veinte", "treinta", "cuarenta", "cincuenta",
                "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "ciento", "doscientos", "trescientos", "cuatrocientos",
                "quinientos", "seiscientos", "setecientos", "ochocientos",
                "novecientos"]

    if n == 0:
        return "cero"

    partes = []

    if n >= 1_000_000_000_000:
        partes.append(numero_a_texto(n // 1_000_000_000_000) + " billones")
        n %= 1_000_000_000_000
    if n >= 1_000_000_000:
        partes.append(numero_a_texto(n // 1_000_000_000) + " mil millones")
        n %= 1_000_000_000
    if n >= 1_000_000:
        m = n // 1_000_000
        partes.append("un millon" if m == 1 else numero_a_texto(m) + " millones")
        n %= 1_000_000
    if n >= 1000:
        m = n // 1000
        partes.append("mil" if m == 1 else numero_a_texto(m) + " mil")
        n %= 1000
    if n >= 100:
        if n == 100:
            partes.append("cien")
        else:
            partes.append(centenas[n // 100] + (" " + numero_a_texto(n % 100) if n % 100 else ""))
        n = 0
    if n >= 20:
        d, u = divmod(n, 10)
        partes.append(decenas[d] + (" y " + unidades[u] if u else ""))
    elif n > 0:
        partes.append(unidades[n])

    return " ".join(partes)

en_texto = numero_a_texto(resultado)
print("Resultado en texto:")
print(en_texto.upper())

# -----------------------------------------------------------
# CONCEPTO DE PUNTERO (referencia en Python con ctypes)
# ctypes me permite crear variables como en C y obtener
# su direccion de memoria real, igual que un puntero
# se usa solo cuando necesito interactuar con codigo C
# -----------------------------------------------------------
print()
print("-- Uso de ctypes (memoria de bajo nivel) --")
entero_c  = ctypes.c_longlong(resultado)          # variable tipo C
puntero   = ctypes.pointer(entero_c)              # puntero a esa variable
direccion = ctypes.addressof(entero_c)            # direccion en memoria

print("Valor almacenado:      ", entero_c.value)
print("Direccion de memoria:  ", direccion)
print("Valor leido del puntero:", puntero[0])
print()
print("ctypes se usa solo cuando necesito trabajar con codigo C de bajo nivel")