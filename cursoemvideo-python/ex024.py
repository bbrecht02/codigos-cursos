#cidade= str(input("digite o nome de uma cidade:")).split()
#comparação= str("santo")
#if comparação in cidade[0]:
#	print("{} começa com a palavra 'santo' ".format(cidade))
#else:
#	print("{} não começa com a palavra 'santo' ".format(cidade))	


cidade= str(input("digite o nome de uma cidade:\n")).strip().upper()
if "SANTO" in cidade[:5]:
	print("{} começa com a palavra 'santo' ".format(cidade))
else:
	print("{} não começa com a palavra 'santo' ".format(cidade))
