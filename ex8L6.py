a = int(input("Digite um numero menor que 5: "))

while a>5:
    print("O numero deve ser menor que 5!")
    a = int(input("Digite novamente: "))

while a<=20:
    if a % 2 == 0:
        print(a)
    a += 1
