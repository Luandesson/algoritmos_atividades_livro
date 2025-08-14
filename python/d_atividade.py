"""
Programa: Cálculo de combustível usado em uma viagem
Descrição:
O usuário fornece o tempo gasto (TEMPO) e a velocidade média (VELOCIDADE).
O programa calcula:
- DISTÂNCIA ← TEMPO * VELOCIDADE
- LITROS_USADOS ← DISTÂNCIA / 12
Em seguida, apresenta:
- Velocidade média
- Tempo gasto
- Distância percorrida
- Quantidade de litros usada
"""

# Entrada dos dados
tempo = float(input("Informe o tempo gasto da viagem (horas): "))
velocidade = float(input("Informe a velocidade média em (km/h): "))

# Processamento dos dados
distancia = tempo * velocidade
litros_usados = distancia / 12

# Saída de dados
print("==RESUMO DA VIAGEM==")
print("A velocidade média é:", velocidade, "km/h")
print("Tempo gasto:", tempo, "horas")
print("A distancia pecorrida foi:", distancia, "km")
print("Quantidade de litros usados:", litros_usados, "l")

