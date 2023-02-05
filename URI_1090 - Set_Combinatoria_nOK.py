# -*- coding: utf-8 -*-

'''
from itertools import product, permatations, combinations, combinations_with_replacement

Analise Combinatoria
------------------------------------------------------------------------------------------------------------------------
Iterator                            Arguments               Results
------------------------------------------------------------------------------------------------------------------------
product()                           p, q, … [repeat=1]      cartesian product, equivalent to a nested for-loop
permutations()                      p[, r]                  r-length tuples, all possible orderings, no repeated elements
combinations()                      p, r                    r-length tuples, in sorted order, no repeated elements
combinations_with_replacement()     p, r                    r-length tuples, in sorted order, with repeated elements

-------------------------------------------------------------------------------------------
Examples                                    Results
-------------------------------------------------------------------------------------------
product('ABCD', repeat=2)                   AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)                     AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)                     AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)    AA AB AC AD BB BC BD CC CD DD
===========================================================================================

OU as três cartas são iguais, OU as três cartas são diferentes.
'''
from itertools import combinations


def contar_sets_iguais_comb(cartas_na_mesa):
    comb = list(combinations(cartas_na_mesa, 3))
    for i in comb:
        if (i[0] == i[1] == i[2]):
            comb = []
            return i[0]
    return None

def contar_sets_iguais(cartas_na_mesa):
    for idx_a, a in enumerate(cartas_na_mesa[:-2], start=1):
        for idx_b, b in enumerate(cartas_na_mesa[idx_a:-1], start=idx_a+1):
            for idx_c, c in enumerate(cartas_na_mesa[idx_b:]):
                if (a == b == c):
                    return a
    return None

def excluir_cartas(conjunto_cartas, carta):
    for i in range(3):
        conjunto_cartas.remove(carta)


while True:
    cartas = int(input())
    
    if cartas == 0:
        break

    numero_sets = 0
    conjunto = []
    for carta in range(cartas):
        numero, simbolo = input().split(' ')
        conjunto.append(numero[0] + '_' + simbolo[0])
    
    # Procurando ocorrencias iguais
    while True:
        encontrou = contar_sets_iguais(conjunto)
        if not encontrou:
            break
        else:
            numero_sets += 1
            excluir_cartas(conjunto, encontrou)
            if len(conjunto) < 3:
                break

    # Procurando ocorrencias distintas
    if len(conjunto) > 2:
        for idx_a, a in enumerate(conjunto[:-2], start=1):
            for idx_b, b in enumerate(conjunto[idx_a:-1], start=idx_a+1):
                for idx_c, c in enumerate(conjunto[idx_b:]):
                    mao = [a, b, c]
                    num = [i.split('_')[0] for i in mao]
                    des = [i.split('_')[1] for i in mao]
                    if (
                        (
                            (
                                num[0] != num[1] and        # diferenca precisa ser de 1 em 1
                                num[0] != num[2] and 
                                num[1] != num[2]
                            ) and
                            (des[0] == des[1] == des[2])    # igualdade nao precisa ser de 1 em 1
                        ) or
                        (
                            (
                                num[0] != num[1] and
                                num[0] != num[2] and 
                                num[1] != num[2]
                            ) and
                            (
                                des[0] != des[1] and
                                des[0] != des[2] and
                                des[1] != des[2]
                            )
                        )
                    ):
                        numero_sets += 1

    print(numero_sets)


'''
combs = list(combinations(conjunto, 3))
for comb in combs:
    num = [i.split('_')[0] for i in comb]
    des = [i.split('_')[1] for i in comb]
    if (
        (
            (
                num[0] != num[1] and        # diferenca precisa ser de 1 em 1
                num[0] != num[2] and 
                num[1] != num[2]
            ) and
            (des[0] == des[1] == des[2])    # igualdade nao precisa ser de 1 em 1
        ) or
        (
            (
                num[0] != num[1] and
                num[0] != num[2] and 
                num[1] != num[2]
            ) and
            (
                des[0] != des[1] and
                des[0] != des[2] and
                des[1] != des[2]
            )
        )
    ):
        numero_sets += 1

    '''
