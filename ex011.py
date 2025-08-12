# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintà-la.
# Sabendo que cada litro de tinta, pinta uma área de 2m².  alt+0178= ²/ alt+0179= ³
larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
área = larg * alt
print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(larg, alt, área))
tinta = área / 2
print("Para pintar essa parede, você precisará de {}l de tinta.".format(tinta))