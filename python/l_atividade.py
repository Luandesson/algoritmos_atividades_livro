# programa: Converter dolar de um valor lido em real. Solicitar o valor da coação do dolar
# e também a quantidadde de reais disponivel com o usuario e armazenar em memoria o valor
# da conversao antes da apresentação

cotacao = float(input("Qual o valor da cotação do dolar hoje? "))
reais = float(input("Informe o valor em reais que você quer converter? R$ "))

dolares = reais / cotacao

print(f"O valor convertido é: US${dolares:.2f}")
