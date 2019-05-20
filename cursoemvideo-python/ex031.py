distancia= int(input("Digite a distancia da viagem(km) : "))
if distancia<=200:
    valor= float(distancia*0.50)
    print("o total a pegar é {}".format(valor))
else:
    valor= float(distancia*0.45)
    print("o total a pegar é {}".format(valor))