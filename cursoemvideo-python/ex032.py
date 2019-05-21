ano= int(input("Qual o ano a ser analisado?? Digite 0 caso queira analisar o ano atual\n: "))
if ano==0:
	ano= 2019
	if ano%4==0 or ano%400==0:
		print("{} É BISSEXTO".format(ano))
	else:
		print("{} NÃO É BISSEXTO".format(ano))
elif ano%4==0 or ano%400==0:
	print("{} É BISSEXTO".format(ano))
else:
	print("{} NÃO É BISSEXTO".format(ano))

