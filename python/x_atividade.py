# Programa: Elaborar um programa que calcule e armazene uma raiz de
#  base qualquer com índice qualquer.


base = float(input("Digite a base (número que você quer a raiz): "))
indice = float(input("Digite o índice da raiz: "))

resultado = base ** (1 / indice)


print(f"A raiz de índice {indice} da base {base} é: {resultado:.2f}")

