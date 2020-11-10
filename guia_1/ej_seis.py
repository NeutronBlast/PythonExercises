# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que acepte una secuencia de números separados por coma y genere
# un list y un tuple de strings con esos números.
# Por ejemplo: Secuencia de entrada: “3,5,7,23”
# Salida: List: [´3´, ´5´, ´7´, ´23´] Tuple: (´3´, ´5´, ´7´, ´23´)
# ------------------------------------------------------------------------------------------------------------

def seis():
    str_1 = input("Escriba una secuencia de numeros separados por comas\n")
    lst = str_1.split(",")
    tup = tuple(lst)
    print("List: {} Tuple: {}".format(lst, tup))
    return lst
