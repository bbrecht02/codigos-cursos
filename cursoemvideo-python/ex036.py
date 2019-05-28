valorcasa= float(input("qual o valor da casa? "))
salario= float(input("quanto você ganha? "))
anos= int(input("em quantos anos pretende pagar? "))
parcela= valorcasa/ (anos*12)
if parcela > salario*30/100:
    print("emprestimo negado!")
    print("o valor mensal de {:.2f} exede 30% do seu salario".format(parcela))
else:
    print("emprestimo aprovado!")
    print("você irá pagar R${:.2f} mensais".format(parcela))

