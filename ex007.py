#Desenvolva um programa que leia as duas notas de um aluno, calcule e leia sua média.

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunada nota: "))
média = (n1 + n2) / 2
print("A média entre {:.1f} e {:.1f} é igual à {:.1f}.".format(n1, n2, média))
