# Programa: Ler dois valores númericos inteiros, representados pelas variaveis A e B
# Apresentar o resultado armazenado em memória do quadro da diferença do primeiro valor: variavel A
# Em relação ao segundo valor variavel B

# Entrada dos dados
a = int(input("Informe um valor inteiro para A: "))
b = int(input("Informe um valor inteiro para B: "))

# Processamento dos dados
diferenca = a - b
resultado = diferenca * diferenca

# Saida dos dados
print(f"O resultado da diferença é {resultado:.2f}")