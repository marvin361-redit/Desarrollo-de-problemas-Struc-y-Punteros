# ejercicio6.py
# Como programar la imagen (red neuronal convolucional para clasificar CAT y DOG)
# Materia: Estructura de Datos
# Tema: Struct y Punteros en Python

import random  # para simular los valores de la red neuronal
from dataclasses import dataclass  # para crear mi estructura de datos (equivale a struct en C)

# -----------------------------------------------------------
# ESTRUCTURA DE DATOS con dataclass
# esto es equivalente a un struct en C
# agrupa datos heterogeneos (nombre, filtros, kernel, activacion)
# -----------------------------------------------------------
@dataclass
class CapaCNN:
    nombre: str
    filtros: int
    tamanio_kernel: tuple
    activacion: str

# creo las capas de la red neuronal
capa1 = CapaCNN("Capa Convolucional 1", 32,  (3, 3), "ReLU")
capa2 = CapaCNN("Capa Convolucional 2", 64,  (3, 3), "ReLU")
capa3 = CapaCNN("Capa Convolucional 3", 128, (3, 3), "ReLU")

capas = [capa1, capa2, capa3]

print("=" * 50)
print("CLASIFICACION DE IMAGENES: CAT vs DOG")
print("Red Neuronal Convolucional (CNN)")
print("=" * 50)
print()
print("La imagen del PDF muestra como funciona una CNN:")
print("  Entrada -> imagen de un gato o un perro")
print("  Proceso -> varias capas convolucionales extraen caracteristicas")
print("  Salida  -> clasificacion: CAT o DOG")
print()

# muestro la arquitectura de la red
print("Arquitectura de la CNN (estructura de datos CapaCNN):")
for capa in capas:
    print(f"  {capa.nombre}: filtros={capa.filtros}, kernel={capa.tamanio_kernel}, activacion={capa.activacion}")

print()

# simulacion de clasificacion (sin usar tensorflow o pytorch)
def simular_clasificacion(nombre_imagen):
    # genero caracteristicas aleatorias (simulando lo que haria la CNN real)
    caracteristicas = [random.uniform(0, 1) for _ in range(128)]
    promedio = sum(caracteristicas) / len(caracteristicas)

    if promedio > 0.5:
        return "CAT"
    else:
        return "DOG"

print("Simulacion de clasificacion:")
imagenes_prueba = ["imagen_gato_1.jpg", "imagen_perro_1.jpg", "imagen_gato_2.jpg"]

for imagen in imagenes_prueba:
    resultado = simular_clasificacion(imagen)
    print(f"  {imagen:25s} -> {resultado}")

# -----------------------------------------------------------
# CONCEPTO DE PUNTERO (referencia en Python)
# cuando paso un objeto mutable a una funcion y lo modifico,
# el objeto original SI cambia (paso por referencia)
# -----------------------------------------------------------
def agregar_capa(lista_capas, nueva_capa):
    lista_capas.append(nueva_capa)  # modifica el objeto original

nueva = CapaCNN("Capa Densa Final", 1, (1, 1), "Sigmoid")

print()
print("-- Concepto de referencia (puntero) --")
print("Capas antes de llamar la funcion:", len(capas))
agregar_capa(capas, nueva)  # modifica la lista original
print("Capas despues de llamar la funcion:", len(capas))
print("La lista SI se modifico porque es mutable (paso por referencia)")

# -----------------------------------------------------------
# Analisis de complejidad
# -----------------------------------------------------------
print()
print("Analisis de complejidad:")
print("  Capa convolucional : O(n x k^2)  donde n=pixeles, k=kernel")
print("  Clasificacion final: O(f)        donde f=caracteristicas")
print("  La CNN es eficiente porque comparte los pesos entre posiciones")