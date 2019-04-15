from math import hypot
x= float(input("Digite o valor do cateto oposto:\n"))
y= float(input("Digite o valor do cateto adjacente:\n"))
print("A hipotenusa é {:.2f}".format(hypot(x,y)))