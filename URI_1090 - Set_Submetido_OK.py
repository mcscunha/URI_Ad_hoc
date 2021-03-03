# -*- coding: utf-8 -*-

'''
Possiveis set:
1x - 2x - 3x --> OK --> Mesma linha
1x - 2y - 3z --> OK --> Diagonais - direita ou esquerda
Nx - Ny - Nz --> OK --> Mesma coluna
Nx - Nx - Nx --> OK --> Trio de cartas repetidas

Visao de Matriz:
--+---------------------+
  |         N           |
--+---+-----+-----+-----+
x | C |  1  |  2  |  3  |
--+---+-----+-----+-----+
y | Q |  1  |  2  |  3  |
--+---+-----+-----+-----+
z | T |  1  |  2  |  3  |
--+---+-----+-----+-----+
'''

def descartar_num_diferentes(cartas_mesa, num_cartas, simbolo):
    cartas_mesa[simbolo][0] -= num_cartas
    cartas_mesa[simbolo][1] -= num_cartas
    cartas_mesa[simbolo][2] -= num_cartas
    return num_cartas


def descartar(cartas_mesa, num_cartas, numero):
    cartas_mesa['C'][numero[0]] -= num_cartas
    cartas_mesa['Q'][numero[1]] -= num_cartas
    cartas_mesa['T'][numero[2]] -= num_cartas
    return num_cartas


# Numeros e simbolos diferentes ---> Diagonal da matriz a direita
def diagonal_direita(cartas_mesa):
    soma = 0
    if (
        (sum(cartas_mesa['C']) == 0) or 
        (sum(cartas_mesa['Q']) == 0) or 
        (sum(cartas_mesa['T']) == 0) or
        (cartas_mesa['C'][0] == cartas_mesa['Q'][0] == cartas_mesa['T'][0] == 0) or
        (cartas_mesa['C'][2] == cartas_mesa['Q'][2] == cartas_mesa['T'][2] == 0)
    ):
        return soma
    else:
        # Positiva (diagonal a direita)
        op = min(cartas_mesa['C'][0], cartas_mesa['Q'][1], cartas_mesa['T'][2])
        if op: 
            soma += descartar(cartas_mesa, op, [0, 1, 2])
        op = min(cartas_mesa['C'][1], cartas_mesa['Q'][2], cartas_mesa['T'][0])
        if op: 
            soma += descartar(cartas_mesa, op, [1, 2, 0])
        op = min(cartas_mesa['C'][2], cartas_mesa['Q'][0], cartas_mesa['T'][1])
        if op: 
            soma += descartar(cartas_mesa, op, [2, 0, 1])
    return soma


# Numeros e simbolos diferentes ---> Diagonal da matriz a esquerda
def diagonal_esquerda(cartas_mesa):
    soma = 0
    if (
        (sum(cartas_mesa['C']) == 0) or 
        (sum(cartas_mesa['Q']) == 0) or 
        (sum(cartas_mesa['T']) == 0) or
        (cartas_mesa['C'][0] == cartas_mesa['Q'][0] == cartas_mesa['T'][0] == 0) or
        (cartas_mesa['C'][2] == cartas_mesa['Q'][2] == cartas_mesa['T'][2] == 0)
    ):
        return soma
    else:
        # Negativa (diagonal a esquerda)
        op = min(cartas_mesa['C'][2], cartas_mesa['Q'][1], cartas_mesa['T'][0])
        if op: 
            soma += descartar(cartas_mesa, op, [2, 1, 0])
        op = min(cartas_mesa['C'][0], cartas_mesa['Q'][2], cartas_mesa['T'][1])
        if op: 
            soma += descartar(cartas_mesa, op, [0, 2, 1])
        op = min(cartas_mesa['C'][1], cartas_mesa['Q'][0], cartas_mesa['T'][2])
        if op: 
            soma += descartar(cartas_mesa, op, [1, 0, 2])
    return soma


# Mesmo numero e simbolo
def trio_repetido(cartas_mesa):
    soma = 0
    op = cartas_mesa['C'][0] // 3
    cartas_mesa['C'][0] -= op * 3
    soma += op
    op = cartas_mesa['C'][1] // 3
    cartas_mesa['C'][1] -= op * 3
    soma += op
    op = cartas_mesa['C'][2] // 3
    cartas_mesa['C'][2] -= op * 3
    soma += op
    op = cartas_mesa['Q'][0] // 3
    cartas_mesa['Q'][0] -= op * 3
    soma += op
    op = cartas_mesa['Q'][1] // 3
    cartas_mesa['Q'][1] -= op * 3
    soma += op
    op = cartas_mesa['Q'][2] // 3
    cartas_mesa['Q'][2] -= op * 3
    soma += op
    op = cartas_mesa['T'][0] // 3
    cartas_mesa['T'][0] -= op * 3
    soma += op
    op = cartas_mesa['T'][1] // 3
    cartas_mesa['T'][1] -= op * 3
    soma += op
    op = cartas_mesa['T'][2] // 3
    cartas_mesa['T'][2] -= op * 3
    soma += op
    return soma


# Numeros diferentes e mesmo simbolo
def mesma_linha(cartas_mesa):
    soma = 0
    if (cartas_mesa['C'][0] and cartas_mesa['C'][1] and cartas_mesa['C'][2]):
        op = min(cartas_mesa['C'][0], cartas_mesa['C'][1], cartas_mesa['C'][2])
        soma += descartar_num_diferentes(cartas_mesa, op, 'C')
    if (cartas_mesa['Q'][0] and cartas_mesa['Q'][1] and cartas_mesa['Q'][2]):
        op = min(cartas_mesa['Q'][0], cartas_mesa['Q'][1], cartas_mesa['Q'][2])
        soma += descartar_num_diferentes(cartas_mesa, op, 'Q')
    if (cartas_mesa['T'][0] and cartas_mesa['T'][1] and cartas_mesa['T'][2]):
        op = min(cartas_mesa['T'][0], cartas_mesa['T'][1], cartas_mesa['T'][2])
        soma += descartar_num_diferentes(cartas_mesa, op, 'T')
    return soma

# Mesmo numero e simbolos diferentes
def mesma_coluna(cartas_mesa):
    soma = 0
    for i in range(3):
        if (cartas_mesa['C'][i] and cartas_mesa['Q'][i] and cartas_mesa['T'][i]):
            op = min(cartas_mesa['C'][i], cartas_mesa['Q'][i], cartas_mesa['T'][i])
            cartas_mesa['C'][i] -= op
            cartas_mesa['Q'][i] -= op
            cartas_mesa['T'][i] -= op
            soma += op
    return soma


# with open('1090_valores.txt', 'r') as f:
#     linhas = f.readlines()
# linha = 0


while True:
    #cartas = int(linhas[linha])
    cartas = int(input())
    
    if cartas == 0:
        break
    
    # inicializar as variaveis
    original = {
        'C': [0, 0, 0],
        'Q': [0, 0, 0],
        'T': [0, 0, 0],
    }
    numero_sets = 0

    # Completar as variaveis
    for carta in range(cartas):
        #linha += 1
        #n, s = linhas[linha].split(' ')
        n, s = input().split(' ')
        if s[0] == 'c':
            if   n[0] == 'u': original['C'][0] += 1
            elif n[0] == 'd': original['C'][1] += 1
            elif n[0] == 't': original['C'][2] += 1
        elif s[0] == 'q':
            if   n[0] == 'u': original['Q'][0] += 1
            elif n[0] == 'd': original['Q'][1] += 1
            elif n[0] == 't': original['Q'][2] += 1
        elif s[0] == 't':
            if   n[0] == 'u': original['T'][0] += 1
            elif n[0] == 'd': original['T'][1] += 1
            elif n[0] == 't': original['T'][2] += 1

    
    # Analisando...
    # ESSENCIAL
    matriz = {k: list(v) for k, v in original.items()}
    tentativa_1 = (
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        trio_repetido(matriz) + mesma_linha(matriz) +
        mesma_coluna(matriz)
    )

    # ESSENCIAL
    matriz = {k: list(v) for k, v in original.items()}
    tentativa_3 = (
        mesma_linha(matriz) + diagonal_direita(matriz) + 
        diagonal_esquerda(matriz) + trio_repetido(matriz) +
        mesma_coluna(matriz)
    )

    # ESSENCIAL
    matriz = {k: list(v) for k, v in original.items()}
    tentativa_4 = (
        trio_repetido(matriz) + diagonal_direita(matriz) + 
        diagonal_esquerda(matriz) + mesma_linha(matriz) +
        mesma_coluna(matriz)
    )

    # ESSENCIAL
    matriz = {k: list(v) for k, v in original.items()}
    tentativa_5 = (
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        mesma_linha(matriz) + trio_repetido(matriz) +
        mesma_coluna(matriz)
    )

    # ESSENCIAL
    matriz = {k: list(v) for k, v in original.items()}
    tentativa_10 = (
        trio_repetido(matriz) + diagonal_esquerda(matriz) + 
        diagonal_direita(matriz) + mesma_linha(matriz) +
        mesma_coluna(matriz)
    )

    print(
        max(
            tentativa_1
            , tentativa_3
            , tentativa_4
            , tentativa_5
            ,tentativa_10
       )
    )
    #linha += 1
