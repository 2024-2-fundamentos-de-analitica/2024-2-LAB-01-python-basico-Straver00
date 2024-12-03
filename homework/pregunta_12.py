"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = line.replace("\t", " ").strip().split()
            valores = fila[-1].split(",")
            valores = [int(a.split(":")[1]) for a in valores]
            data.append((fila[0], sum(valores)))
        diccionario = {}
        for letra, numero in data:
            if letra not in diccionario:
                diccionario[letra] = numero
            else:
                diccionario[letra] +=numero
        resultado = dict(sorted(diccionario.items()))
        return resultado
print(pregunta_12())