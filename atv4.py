num1 = []
par = []
soma = 0
for c in range(5):
    num1.append(float(input('digite um valor:')))

for c in num1:
    if c % 2 == 0:
        par.append(c)

for c in par:
    soma = soma + c

print(soma)
