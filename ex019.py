''' O professor quer sortear um dos seus 4 alunos para apagar o quadro.'''

from random import choice
n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno : "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print("O(A) aluno(a) escolhido(a) foi {}".format(escolhido))