# Programa: Construir um programa que calcule, armazene e apresente
#  em metros por segundo o valor da velocidade de um projétil
#  que percorre uma distância em quilômetros a um espaço de
#  tempo em minutos. Utilize a fórmula VELOCIDADE ←
#  (DISTÂNCIA * 1000) / (TEMPO * 60)

# Entrada dos dados
distancia = float(input("Informe a distancia percorrido em (km):  "))
tempo = float(input("Informe o tempo percorrido:  "))

# Processamento dos dados
velocidade = (distancia * 1000) / (tempo * 60)

# Saída dos dados
print(f"A velocidade do projétil é de: {velocidade}km/h")