x = int(input("Digite um valor :"))
y = int(input("Digite um valor :"))
z = int(input("Digite um valor :"))

maior=x
if y>maior:
    maior=y
if z>maior:
    maior=z
if maior==y:
    if z>x:
        segundo_maior=z

    else:
        segundo_maior=Y

if maior==x:
    if z>y:
        segundo_maior=z
    else:
        segundo_maior=y
if maior==z:
    if x>y:
        segundo_maior=x
    else:
        segundo_maior=y
while segundo_maior<maior:
    segundo_maior=segundo_maior+1
    print(segundo_maior)
