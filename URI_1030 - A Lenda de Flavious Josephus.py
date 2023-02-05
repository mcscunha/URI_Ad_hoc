# -*- coding: utf-8 -*-

'''
Teste realizado em 22/02/2021
    Iniciado as 10:00 ate 12:00 = 02:00h
    Retorno as 13:30 ate 18:00 = 04:30h
    --------------------------------------
    Total: 06:30h
'''

for rodada in range(int(input())):
    dados = list(map(int, input().split(' ')))
    pessoas = dados[0]
    salto = dados[1]
    lista = [i+1 for i in range(pessoas)]

    pos_atual = 0
    while len(lista) > 1:
        # -1 pq conta-se o elemento corrente
        retirar = pos_atual + salto -1
        
        # Para o caso que a proxima retirada cai fora do vetor
        if retirar > len(lista) -1:
            retirar = retirar % len(lista)
        
        lista.pop(retirar)
        
        # Caso a retirada foi no ultimo elemento, deve-se posicionar o apontador no inicio
        if len(lista) - 1 < retirar:
            pos_atual = 0
        else:
            pos_atual = retirar

    print(f'Case {rodada+1}: {lista[0]}')
