# Programa: Construir um programa que leia um valor numérico inteiro e
#  apresente como resultado armazenado em memória os seus
#  valores sucessor e antecessor

numero = int(input("Digite o numero inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

print(f"O antecessor do numero informado é: {antecessor}")
print(f"O sucessor do numero informado é: {sucessor}")