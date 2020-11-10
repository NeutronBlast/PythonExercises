# ------------------------------------------------------------------------------------------------------------
# Si la suma de todos los números naturales por debajo de 10 que son múltiplos de 3 o 5,
# tenemos 3, 5, 6 y 9. La suma de estos múltiplos es 23. Encuentre la suma de los múltiplos
# de 3 y 5 por debajo de 1000
# ------------------------------------------------------------------------------------------------------------

n = 1000
sum = 0

for i in range(n-1, 0, -1):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print("La suma de los multiplos de {} es {}".format(n, sum))
