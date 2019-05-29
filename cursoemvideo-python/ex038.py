primeiro= int(input("Primeiro número: "))
segundo= int(input("Segundo número: "))
maior= 0
ma= 0 
if primeiro>segundo:
    maior= "primeiro"
    print("O {} numero é o maior".format(maior.upper()))
elif primeiro== segundo:
    print("não existem valores maiores ou menores, os valores são iguais")   
else:
    maior= "segundo"
    print("O {} numero é o maior".format(maior.upper()))


