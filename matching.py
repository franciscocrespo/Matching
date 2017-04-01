import graph as gp

if __name__ == "__main__":

    json = '{"JUAN": {".NET": 3, "PHP": 1}, "PEDRO": {".NET": 2, "PHP": 3}}'

    grafo = gp.Graph(json)
    matrix = grafo.build_matrix()
    grafo.pesos_print(matrix)


    