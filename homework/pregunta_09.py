"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()
    conteo = {}
    for linea in lineas:
        columnas = linea.strip().split("\t")
        diccionario_str = columnas[4]
        pares = diccionario_str.split(",")
        claves_registro = set()
        for par in pares:
            clave, _ = par.split(":")
            claves_registro.add(clave)
        for clave in claves_registro:
            if clave not in conteo:
                conteo[clave] = 0
            conteo[clave] += 1
    return conteo
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
