# Programa: Ler dois valores para a variaveis A e B, e efetuar a troca dos valores de forma que a variavél A possui o valor
# da variavel B e a variavel B passe a possuir o valor da variavel A. Apresentar os dois valores após a efetivação do
# Processamento da troca.

# Entrada dos dados
a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor e B: "))

# Processamento dos dados
auxiliar = a
a = b
b = auxiliar

# Saida dos dados
print(f"O valor de A é: {a}. E o valor de B é: {b}. ")