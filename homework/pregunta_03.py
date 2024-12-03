"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

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
        suma = []
        for i in range(0, len(letras_unicas)):
            suma_letra = 0
            for j in range(0, len(data)):
                if letras_unicas[i] == data[j][0]:
                    suma_letra += int(data[j][1])
            suma.append((letras_unicas[i], suma_letra))
        suma = sorted(suma)
        return suma
