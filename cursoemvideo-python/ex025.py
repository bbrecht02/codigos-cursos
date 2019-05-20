nome= str(input("digite seu nome completo:\n")).strip().upper()
if "SILVA" in nome.split():
	print("Seu nome {} possui 'Silva' nele".format(nome))
else:
	print("Seu nome {} não possui 'Silva' nele".format(nome))	
