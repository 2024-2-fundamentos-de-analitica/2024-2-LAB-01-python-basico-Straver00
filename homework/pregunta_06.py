"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
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
    with open("files/input/data.csv") as file:
        lines = file.readlines()
        data= []
        for line in lines:
            fila = line.replace("\t", " ").strip().split()[-1].split(",")
            for i in fila:
                data.append(i)
        codigos = []
        for i in range(len(data)):
            codigo = data[i].split(":")
            codigos.append((codigo[0], int(codigo[1])))
        diccionario = {}
        for codigo, valor in codigos:
            if codigo not in diccionario:
                diccionario[codigo] = {"min": valor, "max":valor}
            else:
                if valor < diccionario[codigo]["min"]:
                    diccionario[codigo]["min"] = valor
                if valor > diccionario[codigo]["max"]:
                    diccionario[codigo]["max"] = valor
        diccionario = dict(sorted(diccionario.items()))
        resultado = [(clave, diccionario[clave]["min"], diccionario[clave]["max"]) for clave in diccionario]
    return resultado