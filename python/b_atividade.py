# Programa: Conversão de temperatura de Fehrenheit para graus Celsius
# Ler uma temperatura em Fehrenheit e apresenta-la convertida em graus Celsius.
# A fórmula de conversão é C = ((F - 32) * 5) / 9. Sendo  F para Fahrenheit e C para Celsius.

# Entrada dos dados
fehrenheit =  float(input("Informe a temperatura em Fehrenheit: "))

# Proceessamento dos dados

celsius  = ((fehrenheit - 32) * 5) / 9

# Saída dos dados
print(f"A temperatura em graus Celsius é: {celsius:.2f}ºc")