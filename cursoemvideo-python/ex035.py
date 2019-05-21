lado1= float(input("Primeiro segmento: "))
lado2= float(input("Segundo segmento: "))
lado3= float(input("Terceiro segmento: "))
if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado2+lado1:
	print("É UM TRIANGULO")
else:
	print("NÃO É UM TRIANGULO")
