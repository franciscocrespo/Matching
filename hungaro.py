""" Clase para que ejecuta el algoritmo """
from copy import deepcopy

class Hungaro(object):
    """ En esta clase se corre el algoritmo de Matching hungaro """

    def __init__(self, matrix):
        self.matrix = deepcopy(matrix) # Matriz o grafo de entrada
        self.filas = len(self.matrix) # Numero de filas, es una matriz cuadrada
        # Matriz de macheo, tiene un 1 entre los vertices macheados
        self.matriz_matcheo = [[0 for i in range(self.filas)] for i in range(self.filas)]
        self.elementos_matcheados = [self.filas]


    def matching_inicial(self):
        """ Este metodo debuelve el primer matcheo de los vertices.
           O sea, una matríz con un 1 en los vertices matcheados """

        # Primero recorremos la matriz buscando los 0 de cada fila
        for i in range(self.filas): #filas
            for j in range(self.filas): #columnas
                if self.matrix[i][j] == 0:
                    if i == 0: # para la primera fila marcamos el primer 0
                        self.matriz_matcheo[i][j] = 1
                        break
                    else: # para las demas filas chequeamos si ya estan matcheadas las columnas
                        var_w = 0
                        var_count = 0
                        # Vamos viendo las filas anteriores de la columna que contiene un 0
                        # Vemos que no este matcheada la columna que contiene el 0
                        while var_w < i: # recorremos las filas anteriores de esa columna
                            if self.matriz_matcheo[var_w][j] == 1:
                                var_count = var_count + 1 # Si está macheada lo contamos
                            var_w = var_w + 1
                        if var_count > 0: # si está matcheada no la marcamos
                            continue
                        else: # si no está matcheada la marcamos
                            self.matriz_matcheo[i][j] = 1
        return self.matriz_matcheo


    def resultado_matcheo(self, elementos, matriz_origuinal):
        """ Muestra los vértices matcheados con su peso correspondiente """
        var_elem = [0 for w in range(self.filas)]
        for i in range(self.filas):
            var_count = 0
            var_j = 0
            for j in range(self.filas):
                if self.matriz_matcheo[i][j] == 1:
                    var_elem[i] = (elementos[i][j], matriz_origuinal[i][j])
                    var_count = 1
                    var_j = j
            if var_count == 0:
                print('la fila ' + str(elementos[i][var_j][0]) + ' no matcheo\n')
        return var_elem

    def matching_print(self, matrix):
        """ Imprime la matriz con el matcheo, los vertices matcheados aparecen con un 1 """
        var_n = self.filas
        for i in range(var_n):
            print(matrix[i])

