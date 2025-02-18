"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():

    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        lineas = f.readlines()
        
    valores_por_clave = {}
    for linea in lineas:
        columnas = linea.strip().split("\t")
        diccionario_codificado = columnas[4]
        pares = diccionario_codificado.split(",")
        
        for par in pares:
            clave, valor = par.split(":")
            valor = int(valor)
            if clave not in valores_por_clave:
                valores_por_clave[clave] = [valor, valor]
            else:
                if valor < valores_por_clave[clave][0]:
                    valores_por_clave[clave][0] = valor
                if valor > valores_por_clave[clave][1]:
                    valores_por_clave[clave][1] = valor
    resultado = sorted([(clave, min_val, max_val) for clave, (min_val, max_val) in valores_por_clave.items()],
                       key=lambda x: x[0])
    return resultado
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
