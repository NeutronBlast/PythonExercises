# ------------------------------------------------------------------------------------------------------------
# Escriba un programa que reciba un número entero (positivo o negativo) y por la salida lo
# muestre de forma inversa. Ejemplo, entrada: -123, salida: -321
# ------------------------------------------------------------------------------------------------------------

n = int(input("Esciba un numero\n"))
aux_n = n
new_n = 0

div = 1
positive = n <= 0


while aux_n > 0:
    aux_n //= 10
    div *= 10

div = div//10

while n > 0:
    y = n % 10
    n //= 10

    new_n = (y*div) + new_n
    div //= 10

if positive:
    print(new_n)
else:
    print(-new_n)
