print("===================lojinha tops=====================")
valor= float(input("Qual o valor do produto?"))
result= 0
if valor>0:
    print("FORMAS DE PAGAMENTO")
    print("[1] Á vista Dinheiro/Cheque")
    print("[2] Á vista Cartão")
    print("[3] 2x no Cartão")
    print("[4] 3x ou mais no cartão")
    escolha= int(input("Qual sua opção?"))
    if escolha==1:
        result= valor-(valor*(10/100))
        print("Á vista 10% desconto\nTotal a pagar: {}".format(result))
    elif escolha==2:
        result= valor-(valor*(5/100))
        print(result)
    elif escolha==3:
        result= valor/2 
        print(result)
    elif escolha==4:
        vezes= int(input("quantas parcelas?"))
        if vezes<11:
            result= (valor+(valor*20/100))/vezes
            print(result)
        else: 
            print("Tais tirando é?\nVocê não pode parcelar o produto em mais de 10x")

else:
    print ("valor invalido")    



