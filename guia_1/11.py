# ------------------------------------------------------------------------------------------------------------
# Tomando como ejemplo el ejercicio del Fibonacci. Encuentre la suma de los números pares de una serie
# de Fibonacci menores o iguales a 4.000.000
# ------------------------------------------------------------------------------------------------------------

n = 4000000
x = 2
y = 4
sum = 0
serie = [0]

while sum < n:
    sum = x + y
    # print("{}, {} = {}".format(x,y,sum))
    serie.append(y)
    x = y
    y = sum

print(serie)

