from random import shuffle
aluno1= str(input("primeiro aluno:"))
aluno2= str(input("segundo aluno:"))
aluno3= str(input("terceiro aluno:"))
aluno4= str(input("quarto aluno:"))
lista= [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print("A ordem de apresentação será:\n{}".format(lista))