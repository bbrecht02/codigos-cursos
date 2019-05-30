from datetime import *
ano_nascimento= int(input("ano de nascimento: "))
data= date.today().year
idade= data-ano_nascimento
print(idade)
if idade>0 and idade <=9:
    print("Mirim")
elif idade>9 and idade<=14:
    print("Infantil")
elif idade>14 and idade<=19:
    print("Junior")
elif idade>19 and idade<=25:
    print("Senior")
else:
    print("Master")     

