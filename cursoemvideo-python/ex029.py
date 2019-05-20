vel= int(input("Qual a velocidade atual do carro:"))

if vel<=80:
    print("Tenha um bom dia, dirija com segurança!")
elif vel>80:
    ex= int(vel-80)
    print("MULTADO! Você exedeu o limite de 80km/h")
    print("Você devera pagar uma multa de: R${}".format(ex*7))        


