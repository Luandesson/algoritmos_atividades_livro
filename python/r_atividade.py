 # Programa: Em uma eleição sindical concorreram ao cargo de
 #  presidente três candidatos (representados pelas variáveis A,
 #  B e C). Durante a apuração dos votos foram computados
 #  votos nulos e em branco, além dos votos válidos para cada
 #  candidato. Deve ser criado um programa de computador que
 # faça a leitura da quantidade de votos válidos para cada
 #  candidato, além de ler também a quantidade de votos nulos
 #  e em branco. Ao final, o programa deve apresentar o
 #  número total de eleitores, considerando votos válidos, nulos
 #  e em branco; o percentual correspondente de votos válidos
 #  em relação à quantidade de eleitores; o percentual
 #  correspondente de votos válidos do candidato A em relação
 #  à quantidade de eleitores; o percentual correspondente de
 #  votos válidos do candidato B em relação à quantidade de
 #  eleitores; o percentual correspondente de votos válidos do
 #  candidato C em relação à quantidade de eleitores; o
 #  percentual correspondente de votos nulos em relação à
 #  quantidade de eleitores; e, por último, o percentual
 #  correspondente de votos em branco em relação à
 #  quantidade de eleitores. Todos os cálculos devem
 #  efetivamente ser armazenados em memória.



 #Entrada dos dados
candidato_a = int(input("Informe a quantidade de votos para o dandidato A: "))
candidato_b = int(input("Informe a quantidade de votos para o dandidato B: "))
candidato_c = int(input("Informe a quantidade de votos para o dandidato C: "))
voto_branco = int(input(" Informe a quantidade de votos em branco: "))
voto_nulo = int(input(" Informe a quantidade de votos nulo: "))

total = candidato_a + candidato_b + candidato_c + voto_branco + voto_nulo
votos_validos = candidato_a + candidato_b + candidato_c
porcentagem_validos = (votos_validos/total)*100
a = (candidato_a/total)*100
b = (candidato_b/total)*100
c = (candidato_c/total)*100
nulo = (voto_nulo/total)*100
branco = (voto_branco/total)*100

print("===RELATÓRIO DA VOTAÇÃO===")
print("n/ Quantidade de votos: ", total)
print(f"Quantidade de votos validos: {votos_validos},{porcentagem_validos:.2f}%")
print(f"Candidato A, teve {a:.2f}% de votos")
print(f"Candidato B, teve {b:.2f}% de votos")
print(f"Candidato C, teve {c:.2f}% de votos")
print(f"Voto Branco, teve {branco:.2f}%")
print(f"Voto Nulo, teve {nulo:.2f}%")