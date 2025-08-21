# programa :  Elaborar um programa que calcule e apresente o valor do
#  resultado da área de uma circunferência (variável A). O
#  programa deve solicitar a entrada do valor do raio da
#  circunferência (variável R). Para a execução deste
#  problema, utilize a fórmula A ← 3.14159265* R ↑ 2

raio = float(input("Informe o raio: "))
area = 3.14159265*raio**2
print(f"A área é:{area:.2f} ")