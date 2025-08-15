# Programa: Elaborar um programa que apresente o vaor da conversão em real (R$), de um valor lido em dolar (US$).
# O programa deve solicitar ov alor da cotação do dolar e tmbém a quantidade de dolares disponivel com o usuário
# Armazenar em memória o valor da conversão antes da apresentação

# Entrada dos dados
cotacao =  float(input("Informe a cotação do dolar hoje: "))
quantidade_dolares = float(input("Informe a quantidade de dolares para a conversão:  "))

# processamento dos dados
valores_em_reais = cotacao * quantidade_dolares

# Saida dos dados
print("O valor em reais é: R$", valores_em_reais)