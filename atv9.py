#os dicionarios sao parecidos com as tuplas e listas, a diferença e que esses valores nao possuem uma sequencia ordenada 
bob = {
        'nome':'bob',
        'peso':'30',
        'raça':'pitbull',
        'pelagem':'curta',
        }
for x in bob:
    print(x+':'+bob[x])