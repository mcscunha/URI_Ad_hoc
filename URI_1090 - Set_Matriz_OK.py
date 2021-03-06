# -*- coding: utf-8 -*-

'''
Possiveis set:

1x - 2x - 3x --> OK     (x = pode ser Q, C ou T, desde que nao se altere)
1x - 2y - 3z --> OK     (x, y, z = pode ser Q, C ou T, desde que os simbolos nao se repitam)
Nx - Nx - Nx --> OK     (x = pode ser Q, C ou T, desde que o simbolo nao altere)
                        (N = um numero, desde que nao se altere)

Visao de Matriz:
----+-------------------------------+
    |               N               |
----+-------+-------+-------+-------+
x   |   C   |   1   |   2   |   3   |
----+-------+-------+-------+-------+
y   |   Q   |   1   |   2   |   3   |
----+-------+-------+-------+-------+
z   |   T   |   1   |   2   |   3   |
----+-------+-------+-------+-------+

========================================================================
IMPORTANTE: Aprendizado
========================================================================
Para criar uma copia de um dicionario de listas, use:

{key: value[:] for key, value in my_dict.items()}     ou
{key: list(value) for key, value in my_dict.items()}

Se usar:
novo_dict = original.copy()     # Nao funciona se tiver listas dentro

As alteracoes ocorridas nas listas serao repassadas para a nova variavel.
O dicionario novo tem outro ID, mas as listas dentro dele sao reaproveitadas
nesta nova variavel, entao, as mudancas sao refletidas nas duas.

>>> a = {
    'A': [1, 3, 4],
    'B': [3, 6, 9]
}
>>> b = a           # Copia errada! Apenas aponta para o mesmo endereco de memoria
>>> b = a.copy()    # Mesmo problema, apenas cria o dicionario novo!

>>> b['B'] = 2
>>> a
a = {
    'A': [1, 3, 4],
    'B': 2
}
>>> b
b = {
    'A': [1, 3, 4],
    'B': 2
}
>>> id(a)
2103557655485

>>> id(a)
2103557899954

>>> id( a['A'] )
2103557058112

>>> id( b['A'] )
2103557058112

Quando se tem uma lista dentro de outras OU um dicionario de listas, use:

{key: value[:] for key, value in my_dict.items()}     ou
{key: list(value) for key, value in my_dict.items()}
========================================================================
'''

def descartar_num_diferentes(cartas_mesa, num_cartas, simbolo):
    cartas_mesa[simbolo][0] -= num_cartas
    cartas_mesa[simbolo][1] -= num_cartas
    cartas_mesa[simbolo][2] -= num_cartas
    return num_cartas


def descartar(cartas_mesa, num_cartas, numero):
    cartas_mesa[0][numero[0]] -= num_cartas
    cartas_mesa[1][numero[1]] -= num_cartas
    cartas_mesa[2][numero[2]] -= num_cartas
    return num_cartas


# Numeros e simbolos diferentes ---> Diagonal da matriz a direita
def diagonal_direita(cartas_mesa):
    print('Regra da Diagonal - Direita')
    soma = 0
    if (
        ((cartas_mesa[0][0] + cartas_mesa[0][1] + cartas_mesa[0][2]) == 0) or 
        ((cartas_mesa[1][0] + cartas_mesa[1][1] + cartas_mesa[1][2]) == 0) or
        ((cartas_mesa[2][0] + cartas_mesa[2][1] + cartas_mesa[2][2]) == 0) or
        ((cartas_mesa[0][0] + cartas_mesa[1][0] + cartas_mesa[2][0]) == 0) or
        ((cartas_mesa[0][1] + cartas_mesa[1][1] + cartas_mesa[2][1]) == 0) or
        ((cartas_mesa[0][2] + cartas_mesa[1][2] + cartas_mesa[2][2]) == 0)
    ):
        return 0
    else:
        # Positiva (diagonal a direita)
        op = min(cartas_mesa[0][0], cartas_mesa[1][1], cartas_mesa[2][2])
        if op: 
            soma += descartar(cartas_mesa, op, [0, 1, 2])
        op = min(cartas_mesa[0][1], cartas_mesa[1][2], cartas_mesa[2][0])
        if op: 
            soma += descartar(cartas_mesa, op, [1, 2, 0])
        op = min(cartas_mesa[0][2], cartas_mesa[1][0], cartas_mesa[2][1])
        if op: 
            soma += descartar(cartas_mesa, op, [2, 0, 1])
    return soma


# Numeros e simbolos diferentes ---> Diagonal da matriz a esquerda
def diagonal_esquerda(cartas_mesa):
    print('Regra da Diagonal - Negativa')
    soma = 0
    if (
        ((cartas_mesa[0][0] + cartas_mesa[0][1] + cartas_mesa[0][2]) == 0) or 
        ((cartas_mesa[1][0] + cartas_mesa[1][1] + cartas_mesa[1][2]) == 0) or
        ((cartas_mesa[2][0] + cartas_mesa[2][1] + cartas_mesa[2][2]) == 0) or
        ((cartas_mesa[0][0] + cartas_mesa[1][0] + cartas_mesa[2][0]) == 0) or
        ((cartas_mesa[0][1] + cartas_mesa[1][1] + cartas_mesa[2][1]) == 0) or
        ((cartas_mesa[0][2] + cartas_mesa[1][2] + cartas_mesa[2][2]) == 0)
    ):
        return 0
    else:
        # Negativa (diagonal a esquerda)
        op = min(cartas_mesa[0][2], cartas_mesa[1][1], cartas_mesa[2][0])
        if op: 
            soma += descartar(cartas_mesa, op, [2, 1, 0])
        op = min(cartas_mesa[0][0], cartas_mesa[1][2], cartas_mesa[2][1])
        if op: 
            soma += descartar(cartas_mesa, op, [0, 2, 1])
        op = min(cartas_mesa[0][1], cartas_mesa[1][0], cartas_mesa[2][2])
        if op: 
            soma += descartar(cartas_mesa, op, [1, 0, 2])
    return soma


# Mesmo numero e simbolo
def trio_repetido(cartas_mesa):
    print('Regra do Trio de Cartas')
    soma = 0
    op = cartas_mesa[0][0] // 3
    cartas_mesa[0][0] -= op * 3
    soma += op
    op = cartas_mesa[0][1] // 3
    cartas_mesa[0][1] -= op * 3
    soma += op
    op = cartas_mesa[0][2] // 3
    cartas_mesa[0][2] -= op * 3
    soma += op
    op = cartas_mesa[1][0] // 3
    cartas_mesa[1][0] -= op * 3
    soma += op
    op = cartas_mesa[1][1] // 3
    cartas_mesa[1][1] -= op * 3
    soma += op
    op = cartas_mesa[1][2] // 3
    cartas_mesa[1][2] -= op * 3
    soma += op
    op = cartas_mesa[2][0] // 3
    cartas_mesa[2][0] -= op * 3
    soma += op
    op = cartas_mesa[2][1] // 3
    cartas_mesa[2][1] -= op * 3
    soma += op
    op = cartas_mesa[2][2] // 3
    cartas_mesa[2][2] -= op * 3
    soma += op
    return soma


# Numeros diferentes e mesmo simbolo
def mesma_linha(cartas_mesa):
    print('Regra da Mesma Linha')
    soma = 0
    if (cartas_mesa[0][0] and cartas_mesa[0][1] and cartas_mesa[0][2]):
        op = min(cartas_mesa[0][0], cartas_mesa[0][1], cartas_mesa[0][2])
        soma += descartar_num_diferentes(cartas_mesa, op, 0)
    if (cartas_mesa[1][0] and cartas_mesa[1][1] and cartas_mesa[1][2]):
        op = min(cartas_mesa[1][0], cartas_mesa[1][1], cartas_mesa[1][2])
        soma += descartar_num_diferentes(cartas_mesa, op, 1)
    if (cartas_mesa[2][0] and cartas_mesa[2][1] and cartas_mesa[2][2]):
        op = min(cartas_mesa[2][0], cartas_mesa[2][1], cartas_mesa[2][2])
        soma += descartar_num_diferentes(cartas_mesa, op, 2)
    return soma


def mesma_coluna(cartas_mesa):
    print('Regra da Mesma Coluna')
    soma = 0
    for i in range(3):
        if (cartas_mesa[0][i] and cartas_mesa[1][i] and cartas_mesa[2][i]):
            op = min(cartas_mesa[0][i], cartas_mesa[1][i], cartas_mesa[2][i])
            cartas_mesa[0][i] -= op
            cartas_mesa[1][i] -= op
            cartas_mesa[2][i] -= op
            soma += op
    return soma


from time import time
inicio = time()

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

    for carta in range(cartas):
        linha += 1
        n = linhas[linha].split(' ')
        if n[1] == 'c':
            if   n[0] == 'u': original[0][0] += 1
            elif n[0] == 'd': original[0][1] += 1
            elif n[0] == 't': original[0][2] += 1
        elif n[1] == 'q':
            if   n[0] == 'u': original[1][0] += 1
            elif n[0] == 'd': original[1][1] += 1
            elif n[0] == 't': original[1][2] += 1
        elif n[1] == 't':
            if   n[0] == 'u': original[2][0] += 1
            elif n[0] == 'd': original[2][1] += 1
            elif n[0] == 't': original[2][2] += 1

    
    # Analisando...

    print('Original:\n', original[0], '\n', original[1], '\n', original[2], '\n',)

    matriz = [list(j) for j in original]
    print('Tentativa 1\n', '-'*30)
    tentativa_1 = (
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        trio_repetido(matriz) + mesma_linha(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_1}\n')

    matriz = [list(j) for j in original]
    print('Tentativa 2\n', '-'*30)
    tentativa_2 = (
        trio_repetido(matriz) + mesma_linha(matriz) +  
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_2}\n')

    matriz = [list(j) for j in original]
    print('Tentativa 3\n', '-'*30)
    tentativa_3 = (
        mesma_linha(matriz) + diagonal_direita(matriz) + 
        diagonal_esquerda(matriz) + trio_repetido(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_3}\n')

    matriz = [list(j) for j in original]
    print('Tentativa 4\n', '-'*30)
    tentativa_4 = (
        trio_repetido(matriz) + diagonal_direita(matriz) + 
        diagonal_esquerda(matriz) + mesma_linha(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_4}\n')
    
    matriz = [list(j) for j in original]
    print('Tentativa 5\n', '-'*30)
    tentativa_5 = (
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        mesma_linha(matriz) + trio_repetido(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_5}\n')
    
    matriz = [list(j) for j in original]
    print('Tentativa 6\n', '-'*30)
    tentativa_6 = (
        mesma_linha(matriz) + trio_repetido(matriz) + 
        diagonal_direita(matriz) + diagonal_esquerda(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_6}\n')

    # Repetindoo a parte de cima, só invertendo DIAGONAIS DIREITA e ESQUERDA
    matriz = [list(j) for j in original]
    print('Tentativa 7\n', '-'*30)
    tentativa_7 = (
        diagonal_esquerda(matriz) + diagonal_direita(matriz) +
        trio_repetido(matriz) + mesma_linha(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_7}\n')

    matriz = [list(j) for j in original]
    print('Tentativa 8\n', '-'*30)
    tentativa_8 = (
        trio_repetido(matriz) + mesma_linha(matriz) +  
        diagonal_esquerda(matriz) + diagonal_direita(matriz) +
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_8}\n')

    matriz = [list(j) for j in original]
    print('Tentativa 9\n', '-'*30)
    tentativa_9 = (
        mesma_linha(matriz) + diagonal_esquerda(matriz) + 
        diagonal_direita(matriz) + trio_repetido(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_9}\n')

    matriz = [list(j) for j in original]
    print('Tentativa 10\n', '-'*30)
    tentativa_10 = (
        trio_repetido(matriz) + diagonal_esquerda(matriz) + 
        diagonal_direita(matriz) + mesma_linha(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_10}\n')
    
    matriz = [list(j) for j in original]
    print('Tentativa 11\n', '-'*30)
    tentativa_11 = (
        diagonal_esquerda(matriz) + diagonal_direita(matriz) +
        mesma_linha(matriz) + trio_repetido(matriz) + 
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_11}\n')
    
    matriz = [list(j) for j in original]
    print('Tentativa 12\n', '-'*30)
    tentativa_12 = (
        mesma_linha(matriz) + trio_repetido(matriz) + 
        diagonal_esquerda(matriz) + diagonal_direita(matriz) +
        mesma_coluna(matriz)
    )
    print(matriz[0], '\n', matriz[1], '\n', matriz[2])
    print(f'Pontos: {tentativa_12}\n')

    print(cartas, ' ----> ',
        max(
            tentativa_1, tentativa_2, tentativa_3, tentativa_4, 
            tentativa_5, tentativa_6, tentativa_7, tentativa_8,
            tentativa_9, tentativa_10, tentativa_11, tentativa_12
        )
    )
    linha += 1

print(f'Tempo total: {(time() - inicio):0.4f} segundos')
