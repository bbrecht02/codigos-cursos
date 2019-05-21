salario= float(input("Digite seu salario: "))
if salario > 1250:
	aumento= salario*10/100
	print("o novo salario para quem ganhava {} será {:.2f} ".format(salario,salario+aumento))
elif salario <= 1250:
	aumento= salario*15/100
	print("o novo salario para quem ganhava {} será {:.2f} ".format(salario,salario+aumento))

