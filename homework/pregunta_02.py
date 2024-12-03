"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = line.replace("\t", ",").strip().split(",")
            data.append(fila)
        letras = []
        for i in range(0, len(data)):
            letras.append(data[i][0])
        letras_unicas = list(set(letras))
        cantidad = []
        for i in range(0, len(letras_unicas)):
            cantidad.append((letras_unicas[i], letras.count(letras_unicas[i])))
        cantidad = sorted(cantidad)
        return cantidad
