def operaciones_con_juntos(lista1, lista2):
    # Convierte las listas en conjuntos
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Calcula la intersección usando conjuntos
    interseccion = conjunto1.intersection(conjunto2)

    # Calcula la unión usando conjuntos
    union = conjunto1.union(conjunto2)

    # Calcula la diferencia simétrica usando conjuntos
    diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

    # Crea el diccionario con los resultados
    resultados = {
        "interseccion": list(interseccion),
        "union": list(union),
        "diferencia_simetrica": list(diferencia_simetrica)
    }

    return resultados

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]


resultados = operaciones_con_juntos(lista1, lista2)


print("Intersección:", resultados["interseccion"])
print("Unión:", resultados["union"])
print("Diferencia Simétrica:", resultados["diferencia_simetrica"])