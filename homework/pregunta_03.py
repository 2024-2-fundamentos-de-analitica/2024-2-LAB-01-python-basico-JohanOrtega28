"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    suma_por_letra = {}
    for linea in lineas:
        columnas = linea.strip().split("\t")
        letra = columnas[0]
        valor = int(columnas[1])
        if letra not in suma_por_letra:
            suma_por_letra[letra] = 0
        suma_por_letra[letra] += valor
    resultado = sorted(suma_por_letra.items(), key=lambda x: x[0])
    return resultado
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
