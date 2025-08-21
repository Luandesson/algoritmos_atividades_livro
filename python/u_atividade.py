# programa : Elaborar um programa de computador que calcule e
#  apresente o valor do volume de uma esfera. Utilize a fórmula
#  VOLUME ← (4 / 3) * 3.14159 * (RAIO ↑ 3)

# Entrada dos dados
raio = float(input("Informe o raio da esfera: "))

#Processamento dos dados

volume = (4 / 3) * 3.14159 * (raio ** 3)

# Saída dos dados
print(f" o volume da esfera é: {volume:.2f}")