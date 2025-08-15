# Programa: Efetue o calculo e apresentar o valor de uma prestação de um bem em atraso
# Utilizando a fórmula: PRESTAÇÃO = VALOR + (VALOR * (TAXA/100 * TEMPO)

# Entrada dos dados
valor = float(input("Digitte o valor da prestação (em R$): "))
taxa = float(input("Digite o valor da taxa (%): "))
tempo = int(input("Quantos dias em atraso? "))

# Processamento dos dados
prestacao = valor + (valor*(taxa/100 * tempo))

# Saída dos dados
print("O valor da prestação atual é de R$", prestacao)