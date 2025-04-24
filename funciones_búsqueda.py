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

def medir_tiempos_busqueda_lineal(array_longitudes, valor):
        """
        Mide los tiempos de búsqueda lineal para diferentes casos (mejor, medio, peor).

        :param array_longitudes: Lista de longitudes de arrays.
        :param valor: Valor a buscar en los arrays.
        :return: Diccionario con los tiempos de búsqueda para cada caso y longitud.
        """
        tiempos = {"mejor_caso": [], "caso_medio": [], "peor_caso": []}

        for longitud in array_longitudes:
            # Crear un array de ceros con la longitud dada
            array = [0] * longitud

            # Mejor caso: insertar el valor al inicio
            array[0] = valor
            inicio_tiempo = time.time()
            busqueda_lineal(array, valor)
            fin_tiempo = time.time()
            tiempos["mejor_caso"].append(fin_tiempo - inicio_tiempo)

            # Caso medio: insertar el valor en la posición central
            array[0] = 0  # Restaurar el inicio
            array[len(array) // 2] = valor
            inicio_tiempo = time.time()
            busqueda_lineal(array, valor)
            fin_tiempo = time.time()
            tiempos["caso_medio"].append(fin_tiempo - inicio_tiempo)

            # Peor caso: insertar el valor al final
            array[len(array) // 2] = 0  # Restaurar el centro
            array[-1] = valor
            inicio_tiempo = time.time()
            busqueda_lineal(array, valor)
            fin_tiempo = time.time()
            tiempos["peor_caso"].append(fin_tiempo - inicio_tiempo)

        return tiempos

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

def medir_tiempos_busqueda_dicotomica(array_longitudes, valor):
    """
    Mide los tiempos de búsqueda dicotómica para diferentes casos (mejor, medio, peor).

    :param array_longitudes: Lista de longitudes de arrays.
    :param valor: Valor a buscar en los arrays.
    :return: Diccionario con los tiempos de búsqueda para cada caso y longitud.
    """
    tiempos = {"mejor_caso": [], "caso_medio": [], "peor_caso": []}

    for longitud in array_longitudes:
        # Crear un array de ceros con la longitud dada
        array = [0] * longitud

        # Mejor caso: insertar el valor al inicio
        array[0] = valor
        inicio_tiempo = time.time()
        busqueda_dicotomica(array, valor)
        fin_tiempo = time.time()
        tiempos["mejor_caso"].append(fin_tiempo - inicio_tiempo)

        # Caso medio: insertar el valor en la posición central
        array[0] = 0  # Restaurar el inicio
        array[len(array) // 2] = valor
        inicio_tiempo = time.time()
        busqueda_dicotomica(array, valor)
        fin_tiempo = time.time()
        tiempos["caso_medio"].append(fin_tiempo - inicio_tiempo)

        # Peor caso: insertar el valor al final
        array[len(array) // 2] = 0  # Restaurar el centro
        array[-1] = valor
        inicio_tiempo = time.time()
        busqueda_dicotomica(array, valor)
        fin_tiempo = time.time()
        tiempos["peor_caso"].append(fin_tiempo - inicio_tiempo)

    return tiempos

    # Crear un array con 6 valores que se incrementan exponencialmente a partir de 10
array_longitudes = [(10 ** (i+2)) for i in range(6)]
valor_a_buscar = 2

    # Obtener los tiempos de búsqueda lineal
tiempos_lineal = medir_tiempos_busqueda_lineal(array_longitudes, valor_a_buscar)

print("Tiempos de búsqueda lineal:")
for i, longitud in enumerate(array_longitudes):
    print(f"Longitud del array: {longitud}")
    print(f"  Mejor caso: {tiempos_lineal['mejor_caso'][i]:.6f} segundos")
    print(f"  Caso medio: {tiempos_lineal['caso_medio'][i]:.6f} segundos")
    print(f"  Peor caso: {tiempos_lineal['peor_caso'][i]:.6f} segundos")


# Obtener los tiempos de búsqueda dicotómica
tiempos_dicotomica = medir_tiempos_busqueda_dicotomica(array_longitudes, valor_a_buscar)

print("Tiempos de búsqueda dicotómica:")
for i, longitud in enumerate(array_longitudes):
    print(f"Longitud del array: {longitud}")
    print(f"  Mejor caso: {tiempos_dicotomica['mejor_caso'][i]:.6f} segundos")
    print(f"  Caso medio: {tiempos_dicotomica['caso_medio'][i]:.6f} segundos")
    print(f"  Peor caso: {tiempos_dicotomica['peor_caso'][i]:.6f} segundos")

exit(0)
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
