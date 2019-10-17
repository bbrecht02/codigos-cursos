middle = 0
oldman = ""
listaAge = []
cont = 1

for i in range(1 , 5):
    nome = str(input("Nome da pessoa: ")).upper()
    sexo = str(input("Sexo[M/F]: ")).upper()
    idade = int(input("Idade: "))
    listaAge.append(idade)
    if sexo == "M":
        oldman = nome

print("a media de idade é: {}".format((listaAge[0] + listaAge[1] + listaAge[2] + listaAge[3])/4))
print(oldman)
