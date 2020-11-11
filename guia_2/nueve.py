# ------------------------------------------------------------------------------------------------------------
# Escriba una función que reciba como entrada una lista y la salida sea la lista con los
# elementos intercambiados, ejemplo: entrada: [1, 2, 3, 4, 5], salida: [2, 1, 4, 3, 5]
# ------------------------------------------------------------------------------------------------------------

def interchange(lst):
    aux = []
    for i in range(len(lst)):
        if i % 2 == 0 and i < len(lst) - 1:
            aux.append(lst[i + 1])
        elif i % 2 != 0:
            aux.append((lst[i - 1]))
        else:
            aux.append(lst[i])
    return aux
