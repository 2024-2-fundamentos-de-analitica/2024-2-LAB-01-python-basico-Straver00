"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = line.replace("\t", " ").strip().split()
            data.append((fila[1], fila[3].split(",")))
        diccionario = {}
        for numero, letras in data:
            numero = int(numero)
            for letra in letras:
                if letra not in diccionario:
                    diccionario[letra] = numero
                else:
                    diccionario[letra] += numero
        diccionario = dict(sorted(diccionario.items()))
        return diccionario