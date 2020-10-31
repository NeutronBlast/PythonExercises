def seis():
    str_1 = input("Escriba una secuencia de numeros separados por comas\n")
    lst = str_1.split(",")
    tup = tuple(lst)
    print("List: {} Tuple: {}".format(lst, tup))
    return lst
