# ------------------------------------------------------------------------------------------------------------

# Escriba un programa que dado un número n (0 < n ≤ 40), imprima por la pantalla una
# escalera de altura n y base n, usando símbolos “#”. Por ejemplo: entrada n = 4, salida
# (observe que la escalera va de izquierda a derecha):
#       #
#      ##
#     ###
#    ####

# ------------------------------------------------------------------------------------------------------------

n = 0

while n <= 0 or n > 40:
    n = int(input("Escriba un numero entre 1 y 40\n"))

    for i in range(n+1):
        ladder = " " * (n-i) + "#" * i
        print(ladder)
