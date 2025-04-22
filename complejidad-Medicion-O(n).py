import time

# Función de complejidad lineal O(n)
def funcion_lineal(n):
    resultado = 0
    for i in range(n):
        resultado += i
    return resultado

# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_lineal(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_lineal(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos

# Ejecución y muestra de resultados
resultados = medir_tiempos_funcion_lineal([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
for n, tiempo in resultados:
    print(f"n={n:<10} tiempo={tiempo:.6f} segundos")

# Función de complejidad logarítmica O(log n)
def funcion_logaritmica(n):
    resultado = 0
    while n > 1:
        resultado += n
        n //= 2
    return resultado
# Medir tiempos de ejecución con valores incrementales de n
def medir_tiempos_funcion_logaritmica(valores_n):
    tiempos = []
    for n in valores_n:
        inicio = time.time()
        funcion_logaritmica(n)
        fin = time.time()
        tiempos.append((n, fin - inicio))

    return tiempos
# Ejecución y muestra de resultados
resultados_logaritmicos = medir_tiempos_funcion_logaritmica([10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000])
for n, tiempo in resultados_logaritmicos:
    print(f"n={n}, tiempo={tiempo:.6f} segundos")
# Función de complejidad cuadrática O(n^2)
def funcion_cuadratica(n):
    resultado = 0
    for i in range(n):
        for j in range(n):
            resultado += i * j
    return resultado