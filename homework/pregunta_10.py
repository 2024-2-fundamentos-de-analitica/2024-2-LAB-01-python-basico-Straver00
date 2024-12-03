"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = line.replace("\t", " ").strip().split()
            data.append([fila[0], fila[-2], fila[-1]]) 
        resultado = []  
        for dato in data:
            valor1 = len(dato[1].split(","))
            valor2 = len(dato[2].split(","))
            tupla = (dato[0], valor1, valor2)
            resultado.append(tupla)
        return resultado 
print(pregunta_10())
