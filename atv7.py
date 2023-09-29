num1 = []
indice = 0
menor = 1000000

for c in range(5):
    num1.append(float(input('digite um valor:')))

    if num1[c] < menor:
        menor = num1[c]
        indice = c

print('o menor número dos digitados é:', menor,'e seu índice é:',indice)     
