n = 0

while n <= 0 or n > 40:
    n = int(input("Escriba un numero entre 1 y 40\n"))

    for i in range(n+1):
        ladder = " " * (n-i) + "#" * i
        print(ladder)
