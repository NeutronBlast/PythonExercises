# ------------------------------------------------------------------------------------------------------------
# Escriba un generador usando una compresión de lista para indicar en una lista de enteros
# cuales son pares y cuales impares, por ejemplo, entrada: [1, 2, 3 , 4] salida: [“impar”, “par”,
# “impar”, “par”]. Ayuda: recuerde la forma abreviada del if
# ------------------------------------------------------------------------------------------------------------

def generate_par_impar(lst):
    yield ["Impar" if x % 2 != 0 else "Par" for x in lst]


def print_obj(gen_obj):
    for i in gen_obj:
        print(i)
