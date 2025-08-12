#Crie um programa que mostre quanto dinheiro uma pessoa tem na carteira e quantos dólares e euros ela pode comprar.
# US$ = 5,50 / EUR = 6,35
real = float(input("Quanto dinheiro você tem na carteira?R$ "))
dolar = real / 5.50
euro = real / 6.35
print("Com R${} você pode comprar US$ {:.2f} ou EUR {:.2f}".format(real, dolar, euro))
