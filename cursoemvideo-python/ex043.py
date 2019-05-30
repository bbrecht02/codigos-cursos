kg= float(input("Qual seu peso?(kg)"))
h= float(input("Qual sua altura?(m)"))
imc= kg/(h**2)
print ("{:.1f}".format(imc))
if imc<18.5:
    print("voce esta ABAIXO DO PESO")
elif imc>18.5 and imc<=25:
    print("Seu peso esta NORMAL")   
elif imc>25 and imc<=30:
    print("voce esta em SOBREPESO")
elif imc>30 and imc <=40:
    print("Voce esta em OBESIDADE")
else:
    print("Voce esta em OBESIDADE MORBIDA")

