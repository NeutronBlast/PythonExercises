# ------------------------------------------------------------------------------------------------------------
# Escriba una función llamada sumNumbers(), que reciba como entrada un string que
# contiene caracteres numéricos y la salida muestre la suma de tales valores. Ejm: entrada:
# abc1234xyz, la salida debe ser 1234; entrada = aa11b33, salida 44; entrada: pueblo, salida
# 0
# ------------------------------------------------------------------------------------------------------------

def sumNumbers(entrada):
    salida = ""
    for i in [char for char in entrada]:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            salida += i

    return salida



