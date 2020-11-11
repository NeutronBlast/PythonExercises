# ------------------------------------------------------------------------------------------------------------
# Escriba una función llamada delete_duplicates(), que reciba una lista con varios elemento
# duplicados y la salida sea la lista sin duplicados. Ejm: lista de entrada [12, 24, 12, 56, 3, 14,
# 56, 3, 12], la salida debe ser [12, 24, 56, 3, 14]
# ------------------------------------------------------------------------------------------------------------

def delete_duplicates(lst):
    return list(set(lst))
