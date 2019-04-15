from sys import exit
from random import shuffle
#
try:
    alunos = []
    posição = ['primeiro', 'segundo', 'terceiro', 'quarto']
    i = 0
    for x in range(4):
        alunos.insert(i, input('Nome do {} aluno: '.format(posição[i]).strip()))
        if len(alunos[i]) < 2 or not alunos[i].isalpha():
            print('É preciso inserir um nome!')
            exit()
        else:
            i += 1

except:
    print('Erro gerado, script encerrado!')
    exit()

else:
    print('Os nomes dos alunos são:')
    print(alunos)
    print('Mas a ordem de apresentação é: ')
    shuffle(alunos)
    print('Função shuffle(): {}'.format(alunos))
    alunos.sort()
    print('Método sort(): {}'.format(alunos))
    alunos.reverse()
    print('Método reverse(): {}'.format(alunos))