# Programa: Conversão de Celsius para Fahrenheit
# Ler uma temperatura em graus Celsius e apresentá-la convertido em graus Fahrenheit.
# Fórmula: F = (C * 9 / S) + 32

# Entrada dos dados
celsius = float(input("Digite a temperatura em graus Celsius:"))

# Processamento
fahrenheit = (celsius * 9 / 5) + 32

# Saida de dados
print(f"A temperatura em Fahrenheit é: {fahrenheit:.2f}ºF")
