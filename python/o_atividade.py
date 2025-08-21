#  Elaborar um programa que leia quatro valores numéricos
#  inteiros (variáveis A, B, C e D). Ao final, o programa deve
#  apresentar o resultado, armazenado em memória, do
#  produto (variável P) do primeiro com o terceiro valor, e o
#  resultado da soma (variável S) do segundo com o quarto
#  valor.

a = int(input("Informe o valor inteiro de A: "))
b = int(input("Informe o valor inteiro de B: "))
c = int(input("Informe o valor inteiro de C: "))
d = int(input("Informe o valor inteiro de D: "))

p = a * c
s = b * d

print(f"O valor de P é: {p}, e o valor de S é: {s}")