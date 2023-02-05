# -*- coding: utf-8 -*-

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
