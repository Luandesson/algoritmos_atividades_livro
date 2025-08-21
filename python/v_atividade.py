# Programa: Elaborar um programa que leia dois valores numéricos
#  inteiros, os quais devem representar a base e o expoente de
#  uma potência, calcular a potência, armazenar em memória o
# resultado calculado e apresentar o resultado obtido.

# Entrada dos dados
base = int(input("Informe o valor inteiiro da base:  "))
expoente = int(input("Informe o valor inteiro do expoente:  "))

# Processamento dos dados
resultado = base ** expoente

# Saida dos dados
print(f"O resultado da potencia é: {resultado:.2f}")