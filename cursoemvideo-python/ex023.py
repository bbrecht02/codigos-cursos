n= int(input("digite um numero de 0 a 9999:\n"))
u= n// 1%10
d= n// 10%10
c= n// 100%10
m= n// 1000%10
print("a unidade desse numero é: {}".format(u))
print("a dezena desse numero é: {}".format(d))
print("a centena desse numero é: {}".format(c))
print("a milhar desse numero é: {}".format(m))
