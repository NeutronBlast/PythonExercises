n = 100
x = 2
y = 4
sum = 0
serie = [0]

while (sum < n):
    sum = x + y
    # print("{}, {} = {}".format(x,y,sum))
    serie.append(y)
    x = y
    y = sum

print(serie)
