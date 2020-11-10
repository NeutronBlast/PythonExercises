# ------------------------------------------------------------------------------------------------------------
# Escriba una función llamada primeOrComposite(), que reciba como argumento un número
# n positivo y la salida sea Primo si es primo o Compuesto si no lo es, Ejm: entrada 47, salida
# Primo, entrada 16, salida Compuesto.
# ------------------------------------------------------------------------------------------------------------

def primeOrComposite(n):
    prime = "Primo"
    for i in range(2, n // 2):
        if n % i == 0:
            prime = "Compuesto"
            break
    return prime


numero = int(input("Ingrese un numero\n"))
print(primeOrComposite(numero))
