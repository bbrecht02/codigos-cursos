from datetime import date
ano= int(input("Ano de nascimento:"))
data= date.today().year
idade= data-ano
alistamento= int(18)
distancia= 0
if ano>18:
    distancia= idade-18
elif ano<18:
    distancia= 18-idade
else:
    distancia= 0  
  
ano_alistamento= data-distancia


if ano_alistamento >2019:
    print("em {} quem nasceu em {} tinha {} anos".format(data,ano, idade))
    print("você deverá se alistar daqui a {} anos".format(abs(distancia)))
    print("Seu alistamento será em {}".format(ano_alistamento))
elif ano_alistamento==2019:
    print("em {} quem nasceu em {} tinha {} anos".format(data,ano, idade))
    print("você deverá se alistar esse ano")
    print("Seu alistamento será em {}".format(ano_alistamento))
else:
    print("em {} quem nasceu em {} tinha {} anos".format(data,ano, idade))
    print("você deveria ter se alistado há {} anos atrás".format(distancia))
    print("Seu alistamento será em {}".format(ano_alistamento))


