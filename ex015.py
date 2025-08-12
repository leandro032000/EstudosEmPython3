# carro custa R$60 por dia mais R$0.15 por km rodado.

dias = int(input("Quantos dias o carro ficou alugado? "))
km = float(input("Quantos km rodados? "))
pago = (dias * 60) + (km * 0.15)
print("O total a pagar pelo valor do aluguel do carro é de {:.2f}.".format(pago))
