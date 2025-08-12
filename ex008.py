#Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e em milímetros.
# km hm dcm m dm cm mm
medida = float(input("Digite uma distância em metros: "))
km = medida / 1000
cm = medida * 100
mm = medida * 1000
print("À medida de {}m corresponde à {}km, à {:.0f}cm e à {:.0f}mm".format(medida, km, cm, mm))
