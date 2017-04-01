import graph as gp
import hungaro as hu

if __name__ == "__main__":

    #__json__ = '{"JUAN": {".NET": 3, "PHP": 1}, "PEDRO": {".NET": 2, "PHP": 3}}'
    __json__ = '{"A": {"I": 1, "II": 2, "III": 5, "IV": 5, "V": 3, "VI": 8, "VII": 2, "VIII": 9}, "B": {"I": 9, "II": 8, "III": 8, "IV": 9, "V": 8, "VI": 8, "VII": 1, "VIII": 3}, "C": {"I": 3, "II": 1, "III": 5, "IV": 8, "V": 9, "VI": 6, "VII": 5, "VIII": 8}, "D": {"I": 9, "II": 1, "III": 7, "IV": 9, "V": 3, "VI": 8, "VII": 8, "VIII": 5}, "E": {"I": 8, "II": 9, "III": 2, "IV": 4, "V": 8, "VI": 5, "VII": 9, "VIII": 9}, "F": {"I": 9, "II": 8, "III": 3, "IV": 8, "V": 8, "VI": 9, "VII": 8, "VIII": 1}, "G": {"I": 5, "II": 4, "III": 8, "IV": 9, "V": 1, "VI": 8, "VII": 9, "VIII": 8}, "H": {"I": 8, "II": 8, "III": 9, "IV": 1, "V": 8, "VI": 3, "VII": 1, "VIII": 1}}'

    print('\nMATRIZ DE PESOS ORIGINALES:\n')
    __grafo__ = gp.Graph(__json__)
    __matrix__ = __grafo__.construir_matriz()
    __grafo__.pesos_print()
    __elementos__ = __grafo__.elementos_del_matching()
    __pesos__ = __grafo__.matriz_pesos()

    __matching__ = hu.Hungaro(__matrix__)
    __elementos_match__ = __matching__.matching_inicial()
    print('\nMATRIZ DE PRIMER MATCHEO:\n')
    __matching__.matching_print(__elementos_match__)

    print('\nELEMENTOS MATCHEADOS:\n')
    __resultado__ = __matching__.resultado_matcheo(__elementos__, __pesos__)

    print(__resultado__)


    