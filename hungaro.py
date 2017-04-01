""" Clase para que ejecuta el algoritmo """
from copy import deepcopy

class Hungaro(object):
    """ En esta clase se corre el algoritmo de Matching hungaro """

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)
        self.filas = len(self.matrix)

    def matching_inicial(self):
        """ Este metodo debuelve el primer matcheo de los vertices.
           O sea, una matríz con un 1 en los vertices matcheados """

        # Primero recorremos la matriz buscando los 0 de cada fila
        elementos_matcheados = [[0 for i in range(self.filas)] for i in range(self.filas)]
        for i in range(self.filas): #filas
            for j in range(self.filas): #columnas
                if self.matrix[i][j] == 0:
                    if i == 0: # para la primera fila marcamos el primer 0
                        elementos_matcheados[i][j] = 1
                        break
                    else: # para las demas filas chequeamos si ya estan matcheadas las columnas
                        var_w = 0
                        var_count = 0
                        # Vamos viendo las filas anteriores de la columna que contiene un 0
                        # Vemos que no este matcheada la columna que contiene el 0
                        while var_w < i: # recorremos las filas anteriores de esa columna
                            if self.matrix[var_w][j] == 1:
                                var_count = var_count + 1 # Si está macheada lo contamos
                            var_w = var_w + 1
                        if var_count > 0: # si está matcheada no la marcamos
                            continue
                        else: # si no está matcheada la marcamos
                            elementos_matcheados[i][j] = 1
        return elementos_matcheados

    def matching_print(self, matrix):
        """ Imprime la matriz """
        print(matrix)