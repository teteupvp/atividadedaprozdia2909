#a diferença entre listas e tuplas é uqe nas tuplas as os valores atribuídos podem mudarm enquanto nas listas não.
#Um vetor, ao ser criado, já tem o tamanho pré-determinado na criação, não podendo mais ser alterado. as tuplas e listas  posssuem valores a determin

num1 = []
maior = 0
menor = 0

for c in range(5):
    num1.append(float(input('digite um valor:')))

for c in num1:
    if maior == 0:
        maior = c

    if c > maior:
        maior = c    

    if menor == 0:
        menor = c
    if c < menor:
        menor = c

print(maior - menor)
