valor= float(input("Qual o valor do produto? R$\n"))
porc= valor*5/100
newvalor= valor-porc
print("O produto no valor de R${} ficará por R${} com 5% de desconto".format(valor,newvalor))