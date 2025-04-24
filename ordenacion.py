# El algoritmo de ordenación por burbuja es un algoritmo de ordenación simple que compara elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que el array está ordenado.
import random
import time
def ordenacion_burbuja(array):
    """
    Ordena un array de números usando el algoritmo de ordenación por burbuja.

    :param array: Lista de números a ordenar.
    :return: Lista ordenada de menor a mayor.
    """
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                array[j], array[j+1] = array[j+1], array[j]
    return array

def medir_tiempos_ordenacion_burbuja(longitudes):
        """
        Crea arrays de las longitudes especificadas, los inicializa aleatoriamente,
        los ordena usando el algoritmo de burbuja y mide el tiempo invertido.

        :param longitudes: Lista de longitudes de los arrays a generar.
        :return: Lista de tuplas (longitud, tiempo_invertido).
        """
        resultados = []
        for longitud in longitudes:
            # Crear un array aleatorio de la longitud especificada
            array = [random.randint(0, 100) for _ in range(longitud)]
            # Medir el tiempo antes y después de la ordenación
            inicio = time.time()
            ordenacion_burbuja(array)
            fin = time.time()
            # Calcular el tiempo invertido
            tiempo_invertido = fin - inicio
            # Guardar el resultado
            resultados.append((longitud, tiempo_invertido))
        return resultados

def ordenación_quicksort(array):
            """
            Ordena un array de números usando el algoritmo quicksort y explica cada paso.

            :param array: Lista de números a ordenar.
            :return: Lista ordenada de menor a mayor.
            """
            if len(array) <= 1:
                # Si el array tiene 0 o 1 elementos, ya está ordenado
                print(f"Array {array} ya está ordenado o tiene un solo elemento.")
                return array
            else:
                # Elegir el pivote como el elemento central
                pivot = array[len(array) // 2]
                print(f"Elegimos el pivote: {pivot}")
                
                # Dividir el array en tres partes: menores, iguales y mayores
                menores = [x for x in array if x < pivot]
                iguales = [x for x in array if x == pivot]
                mayores = [x for x in array if x > pivot]
                
                print(f"Elementos menores que el pivote {pivot}: {menores}")
                print(f"Elementos iguales al pivote {pivot}: {iguales}")
                print(f"Elementos mayores que el pivote {pivot}: {mayores}")
                
                # Recursivamente ordenar las partes menores y mayores
                return ordenación_quicksort(menores) + iguales + ordenación_quicksort(mayores)


longitudes = [10, 100, 1000, 10000]
resultados = medir_tiempos_ordenacion_burbuja(longitudes)
for longitud, tiempo in resultados:
    print(f"Longitud: {longitud>10} Tiempo invertido: {tiempo:.6f} segundos")



