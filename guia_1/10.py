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

