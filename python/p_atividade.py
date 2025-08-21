# Programa: Elaborar um programa que leia o valor numérico
#correspondente ao salário mensal (variável SM) de um  trabalhador e também fazer a leitura do valor do percentual
# de reajuste (variável PR) a ser atribuído. Apresentar o valor
# do novo salário (variável NS) após o armazenamento do cálculo em memória.

sm = float(input("Informe o salario mensal: R$"))
pr = float(input("Informe o porcentual de reajuste (%): "))

novo_salario = sm+(sm*pr/100)
print("Seu novo salário é: R$",novo_salario)