import random
import time

def busqueda_lineal(array, valor):
    """
    Realiza una búsqueda lineal en un array.

    :param array: Lista de valores numéricos.
    :param valor: Valor a buscar en el array.
    :return: Índice del valor si se encuentra, de lo contrario -1.
    """
    for i in range(len(array)):
        if array[i] == valor:
            return i
    return None



def busqueda_dicotomica(array, valor):
    """
    Realiza una búsqueda dicotómica en un array ordenado.

    :param array: Lista de valores numéricos ordenados.
    :param valor: Valor a buscar en el array.
    :return: Índice del valor si se encuentra, de lo contrario -1.
    """
    inicio = 0
    fin = len(array) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if array[medio] == valor:
            return medio
        elif array[medio] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None
# Ejemplo de uso
# Crear un array con 10 enteros positivos aleatorios entre 0 y 20

n = 100  # Cambia este valor para probar con diferentes tamaños
array = [0] * n  # Inicialmente lleno de ceros

for i in len(array):
    array[i]= random.randint(0, 20)

array = sorted(array)
valor_a_buscar = 10  # Cambia este valor para probar con diferentes valores

print("Array:", array)
print("Valor a buscar:", valor_a_buscar)


# Medir el tiempo antes de la búsqueda lineal
inicio_tiempo_lineal = time.time()
# Llamar a la función de búsqueda lineal
resultado_lineal = busqueda_lineal(array, valor_a_buscar)
fin_lineal = time.time()  # Tiempo después de la llamada
# Calcular el tiempo invertido
tiempo_invertido_lineal = fin_lineal - inicio_tiempo_lineal

# Imprimir el resultado de la búsqueda lineal
if resultado_lineal is not None:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {resultado_lineal} (búsqueda lineal).")
    print(f"Tiempo invertido (búsqueda lineal): {tiempo_invertido_lineal:.6f} segundos.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en el array (búsqueda lineal).")
    print(f"Tiempo invertido (búsqueda lineal): {tiempo_invertido_lineal:.6f} segundos.")



# Medir el tiempo antes de la búsqueda
inicio_tiempo = time.time()
# Llamar a la función de búsqueda dicotómica
resultado = busqueda_dicotomica(array, valor_a_buscar)
fin = time.time()  # Tiempo después de la llamada
# Calcular el tiempo invertido
tiempo_invertido = fin - inicio_tiempo

# Imprimir el resultado de la búsqueda dicotómica
if resultado is not None:
    print(f"El valor {valor_a_buscar} se encuentra en el índice {resultado} (búsqueda dicotómica).")
    print(f"Tiempo invertido (búsqueda dicotómica): {tiempo_invertido:.6f} segundos.")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en el array (búsqueda dicotómica).")
    print(f"Tiempo invertido (búsqueda dicotómica): {tiempo_invertido:.6f} segundos.")
