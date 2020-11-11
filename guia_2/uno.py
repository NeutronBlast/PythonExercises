# ------------------------------------------------------------------------------------------------------------

# Escriba un programa que reciba como entrada un número entero n mayor a 0, y la salida sea de la forma 123…n,
# donde … son los números que faltan en la secuencia. Ejemplo:
# Si la entrada n = 5, la salida es 12345

# ------------------------------------------------------------------------------------------------------------

def secuencia():
    n = int(input("Escriba un número\n"))
    merged = ""
    for i in range(n, 0, -1):
        merged += str(i)

    print("La secuencia es:", merged)