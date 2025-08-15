# Programa: Combinações de Adições e Multiplicações entre 4 valores
# Ler quatro valores inteiros (A, B, C, D) e apresentar:
# - As 6 adições possíveis: A+B, A+C, A+D, B+C, B+D, C+D
# - As 6 multiplicações possíveis: A*B, A*C, A*D, B*C, B*D, C*D
# A ideia é usar a lógica da distributiva para explorar todas as combinações entre os números.

# Entrada do dados

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))
d = int(input("Informe o valor de D: "))

# Saida dos dados
ab = a + b
ac = a + c
ad = a + d
bc = b + c
bd = b + d
cd = c + d

ab_m = a * b
ac_m = a * c
ad_m = a * d
bc_m = b * c
bd_m = b * d
cd_m = c * d

# Saida dos dados
print("Os resultados das adições são: ", ab, ac, ad, bc, bd, cd)
print("Os valores das multiplicações são: ", ab_m, ac_m, ad_m, bc_m, bd_m, cd_m)