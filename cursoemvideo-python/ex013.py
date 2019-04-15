s= float(input("Qual o salário do funcionário\nR$"))
porc= s*15/100
a= s+porc
print("Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}".format(s,a))