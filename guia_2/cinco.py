# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que dado una lista de tuples que representan un nombre y una edad,
# encontrar la persona de mayor edad. Ejm: [(“Antonio”, 21), (“Roberto”, 18), (“Teresa”, 19)],
# la salida debe ser: Antonio 21
# ------------------------------------------------------------------------------------------------------------

def max_age():
    lst = [("Antonio", 21), ("Roberto", 18), ("Teresa", 19)]
    return sorted(lst, key=lambda x: x[1], reverse=True)[0]
