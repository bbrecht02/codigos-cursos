lado1= float(input("Primeiro segmento: "))
lado2= float(input("Segundo segmento: "))
lado3= float(input("Terceiro segmento: "))
if lado1<lado2+lado3 and lado2<lado1+lado3 and lado3<lado1+lado2:
    print("É UM TRIANGULO!")
    if lado1==lado2 or lado1==lado3:
        print("isosceles")
    elif lado1==lado2 and lado1==lado3:
        print("equilatero")
    elif lado1!=lado2 and lado1!=lado3:
        print("escaleno")
else:
    print("NÃO É UM TRIANGULO!")
    
            


        
