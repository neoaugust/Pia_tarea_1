numeros_enteros=[4, -1, 2, 4, 3, -5, 2 ]

def procesar_numeros_enteros(numeros_enteros):
    for numero in numeros_enteros:
        if numero <0:
            numeros_enteros.remove(numero)
    sin_repetir_y_ordenados=sorted(list(set(numeros_enteros)))
    return sin_repetir_y_ordenados

print(procesar_numeros_enteros(numeros_enteros))

    



