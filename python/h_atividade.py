# Programa: Calcule e apresente o valor do volume de uma caixa retangular
# Utilizando a fórmula: VOLUME = COMPRIMENTO * LARGURA * ALTURA

# Entrada dos dados
comprimento = float(input("Informe o comprimento da caixa retangular: "))
largura = float(input("Informe o largura da caixa retangular: "))
altura = float(input("Informe a altura da caixa retangular: "))

# Processamento dos dados
volume = comprimento * largura * altura

# Saida dos dados
print(f"O volume da caixa retangular é de: {volume:.2f}³.")