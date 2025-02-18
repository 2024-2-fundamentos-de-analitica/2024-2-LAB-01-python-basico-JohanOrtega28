"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()

    suma_por_letra = {}

    for linea in lineas:
        columnas = linea.strip().split("\t")
        valor = int(columnas[1])
        letras = columnas[3].split(",")
        for letra in letras:
            if letra not in suma_por_letra:
                suma_por_letra[letra] = 0
            suma_por_letra[letra] += valor

    resultado = {letra: suma_por_letra[letra] for letra in sorted(suma_por_letra)}
    
    return resultado
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
