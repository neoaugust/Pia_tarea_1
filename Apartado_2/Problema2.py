import string

lista_palabras =["caso","práctico","elena","de","almacén","clientes"]
ruta_archivo = "Prueba.txt"

def contar_frecuencia_palabras(lista_palabras, ruta_archivo):
    # Inicializa un diccionario para almacenar la frecuencia
    frecuencias = {palabra: 0 for palabra in lista_palabras}

    # Lee el contenido del archivo
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Elimina signos de puntuación y convierte a minúsculas
    contenido = contenido.translate(str.maketrans('', '', string.punctuation)).lower()

    # Cuenta la frecuencia de cada palabra en la lista
    for palabra in lista_palabras:
        frecuencia = contenido.count(palabra)
        frecuencias[palabra] = frecuencia

    return frecuencias

# Función para mostrar la frecuencia de forma ordenada
def mostrar_frecuencia_ordenada(frecuencias):
    for palabra in sorted(frecuencias.keys()):
        print(f"{palabra}: {frecuencias[palabra]}")




# Contar la frecuencia
frecuencias = contar_frecuencia_palabras(lista_palabras, ruta_archivo)

# Mostrar la frecuencia
mostrar_frecuencia_ordenada(frecuencias)