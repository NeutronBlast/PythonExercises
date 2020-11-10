# ------------------------------------------------------------------------------------------------------------
# La serie de Fibonacci es aquella que se genera como la suma de los dos números anteriores.
# Por ejemplo, la serie para los números menores a 100 sería:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Escriba un programa que acepte de un usuario un número entero, e indique por la salida los
# números de la serie de Fibonacci menores al número ingresado.
# ------------------------------------------------------------------------------------------------------------

n = int(input("Escriba un numero entero\n"))
x = 0
y = 1
sum = 0
serie = [0]

while sum < n:
    sum = x + y
    # print("{}, {} = {}".format(x,y,sum))
    serie.append(y)
    x = y
    y = sum

print(serie)

