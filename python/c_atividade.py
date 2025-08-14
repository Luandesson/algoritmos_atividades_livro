# Calcular e apresentar o valor do volume de uma lata de óleo utilizando a fórmula
# VOLUME = 3.14159*R**2*ALTURA

#Entrada dos dados
r = float(input("Digite o raio da lata (em cm): "))
altura = float(input("Digite a altura da lata (em cm): "))

# Processamento dos dados
volume = 3.14159 * r**2 * altura

# Saida dos dados
print("O volume da lata de óleo é:", volume, "cm³")