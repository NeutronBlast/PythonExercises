# ------------------------------------------------------------------------------------------------------------
# Escriba una función llamada rotate() que reciba como argumento una lista y un entero n y
# rote los elemento de la lista de acuerdo a ese número n. Ejemplo, lista de entrada: [1, 2, 3,
# 4, 5, 6 ] ; n= 2. La salida debe ser [3, 4, 5, 6, 1, 2]
# ------------------------------------------------------------------------------------------------------------

def rotate(lista, n):
    return lista[n:] + lista[:n]