# Faça um algoritmo que leia um sálario de um funcionário e mostre o novo salário com 15% de aumento.
salário = float(input("Qual é o salário do funcionário? R$"))
novo = salário + (salário * 15 / 100)
print("O salário do funcionário que ganhava R${:.2f}, com 15% de aumento passa a ser R${:.2f}.".format(salário, novo))
