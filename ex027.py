"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel = 'Olá mundo'
print(variavel[-8:-2])
print(variavel[:5])
print(len(variavel))
print(variavel[0:9:2])
print(variavel[-1:-10:-2])

# Claro! Vamos destrinchar [i:f:p] (início:fim:passo) de um jeito simples:

# i (início) — de qual índice começar a pegar caracteres. Se deixar vazio, 
# o Python assume o começo (índice 0) ou o final, dependendo da direção do passo.

# f (fim) — até qual índice ir, sem incluir esse índice. É tipo "vai até aqui, mas 
# não pega esse aqui". Se deixar vazio, o Python vai até a outra ponta da string.

# p (passo) — de quanto em quanto ele "pula" a cada caractere, e em qual direção:

# Positivo → anda para a direita (índice crescente)
# Negativo → anda para a esquerda (índice decrescente)
# Se deixar vazio, o padrão é 1 (anda para direita, de 1 em 1)
# Um jeito de visualizar com "Pedro":

# índices:   0    1    2    3    4
# letras:    P    e    d    r    o
# índices:  -5   -4   -3   -2   -1

# Alguns exemplos pra fixar:

# nome[1:4] → começa no índice 1, vai até o 4 sem incluir → "edr"
# nome[:3] → sem início, então começa do 0, vai até o 3 sem incluir → "Ped"
# nome[2:] → começa no 2, sem fim, então vai até o final → "dro"
# nome[::2] → sem início nem fim, passo 2 (pula de 2 em 2) → "Pdo"
# nome[::-1] → sem início nem fim, passo -1 (inverte tudo) → "ordeP"

# A ideia central é: início e fim são posições nos "espaços entre as letras",
#  e o passo decide a direção e o tamanho do salto.
