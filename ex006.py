#Crie um algoritmo que mostre o seu dobro, triplo e a raiz quadrada.
n = int(input("Digite um número: "))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print("Analisando o número {} \nO dobro é {} \nO triplo é {}\n E a raiz quadrada de {} é {:.2f}.".format(n, d, t, n, rq))
print("Analisando o número {} \n O dobro é {} \n O triplo é {} \n E a raiz quadrada de {} é {:.2f}.".format(n, (n*2), (n*3), n, pow(n, (1/2))))