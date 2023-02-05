# -*- coding: utf-8 -*-

from time import time
inicio = time()

# Numeros e simbolos diferentes ---> Diagonal da matriz a direita
def diagonal_direita(cartas_mesa):
    cartas_mesa_transposta = list(zip(*cartas_mesa))
    soma = 0
    if (
        (cartas_mesa[0].count(0) == 3) or 
        (cartas_mesa[1].count(0) == 3) or 
        (cartas_mesa[2].count(0) == 3) or 
        (cartas_mesa_transposta[0].count(0) == 3) or 
        (cartas_mesa_transposta[1].count(0) == 3) or 
        (cartas_mesa_transposta[2].count(0) == 3)
    ):
        return 0
    else:
        # Positiva (diagonal a direita)
        op = min(cartas_mesa[0][0], cartas_mesa[1][1], cartas_mesa[2][2])
        if op: 
            soma += op
            cartas_mesa[0][0] -= op
            cartas_mesa[1][1] -= op
            cartas_mesa[2][2] -= op
        op = min(cartas_mesa[0][1], cartas_mesa[1][2], cartas_mesa[2][0])
        if op: 
            soma += op
            cartas_mesa[0][1] -= op
            cartas_mesa[1][2] -= op
            cartas_mesa[2][0] -= op
        op = min(cartas_mesa[0][2], cartas_mesa[1][0], cartas_mesa[2][1])
        if op: 
            soma += op
            cartas_mesa[0][2] -= op
            cartas_mesa[1][0] -= op
            cartas_mesa[2][1] -= op
    return soma


# Numeros e simbolos diferentes ---> Diagonal da matriz a esquerda
def diagonal_esquerda(cartas_mesa):
    cartas_mesa_transposta = list(zip(*cartas_mesa))
    soma = 0
    if (
        (cartas_mesa[0].count(0) == 3) or 
        (cartas_mesa[1].count(0) == 3) or 
        (cartas_mesa[2].count(0) == 3) or 
        (cartas_mesa_transposta[0].count(0) == 3) or 
        (cartas_mesa_transposta[1].count(0) == 3) or 
        (cartas_mesa_transposta[2].count(0) == 3)
    ):
        return 0
    else:
        # Negativa (diagonal a esquerda)
        op = min(cartas_mesa[0][2], cartas_mesa[1][1], cartas_mesa[2][0])
        if op: 
            soma += op
            cartas_mesa[0][2] -= op
            cartas_mesa[1][1] -= op
            cartas_mesa[2][0] -= op
        op = min(cartas_mesa[0][0], cartas_mesa[1][2], cartas_mesa[2][1])
        if op: 
            soma += op
            cartas_mesa[0][0] -= op
            cartas_mesa[1][2] -= op
            cartas_mesa[2][1] -= op
        op = min(cartas_mesa[0][1], cartas_mesa[1][0], cartas_mesa[2][2])
        if op: 
            soma += op
            cartas_mesa[0][1] -= op
            cartas_mesa[1][0] -= op
            cartas_mesa[2][2] -= op
    return soma


# Mesmo numero e simbolo
def trio_repetido(cartas_mesa):
    soma = 0
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            op = cartas_mesa[j][i] // 3
            cartas_mesa[j][i] -= op * 3
            soma += op
    return soma


# Numeros diferentes e mesmo simbolo
def mesma_linha(cartas_mesa):
    soma = 0
    for i in [0, 1, 2]:
        if cartas_mesa[i].count(0) == 0:
            op = min(cartas_mesa[i])
            soma += op
            for j in [0, 1, 2]:
                cartas_mesa[i][j] -= op
    return soma

# Mesmo numero e simbolos diferentes
def mesma_coluna(cartas_mesa):
    cartas_mesa_transposta = list(zip(*cartas_mesa))
    soma = 0
    for i in [0, 1, 2]:
        if cartas_mesa_transposta[i].count(0) == 0: 
            op = min(cartas_mesa[0][i], cartas_mesa[1][i], cartas_mesa[2][i])
            soma += op
            # ATENCAO: variavel j e i invertidas por ser em colunas
            for j in [0, 1, 2]:
                cartas_mesa[j][i] -= op
    return soma


simbolo = {
    'c': 0, 
    'q': 1, 
    't': 2, 
}
numero = {
    'u': 0, 
    'd': 1, 
    't': 2, 
    }
with open('1090_valores.txt', 'r') as f:
    linhas = f.readlines()
linha = 0

while True:
    cartas = int(linhas[linha])
    
    if cartas == 0:
        break
    
    # inicializar as variaveis
    original = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
    numero_sets = 0

    # Completar as variaveis
    for carta in range(cartas):
        linha += 1
        n = linhas[linha].split(' ')
        original[simbolo[n[1][0]]][numero[n[0][0]]] += 1

    
    # Analisando...
    matriz = [list(j) for j in original]
    tentativa_1 = (
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        trio_repetido(matriz) + mesma_linha(matriz) +
        mesma_coluna(matriz)
    )

    matriz = [list(j) for j in original]
    tentativa_3 = (
        mesma_linha(matriz) + diagonal_direita(matriz) + 
        diagonal_esquerda(matriz) + trio_repetido(matriz) +
        mesma_coluna(matriz)
    )

    matriz = [list(j) for j in original]
    tentativa_4 = (
        trio_repetido(matriz) + diagonal_direita(matriz) + 
        diagonal_esquerda(matriz) + mesma_linha(matriz) +
        mesma_coluna(matriz)
    )

    matriz = [list(j) for j in original]
    tentativa_5 = (
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        mesma_linha(matriz) + trio_repetido(matriz) +
        mesma_coluna(matriz)
    )

    matriz = [list(j) for j in original]
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
            , tentativa_10
       )
    )
    linha += 1

print(f'Tempo total: {(time() - inicio):0.2f} segundos')
