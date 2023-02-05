# -*- coding: utf-8 -*-

while True:
    regioes = int(input())
    if regioes == 0:
        exit(0)

    for salto in range(1, 1000):     # Força Bruta para achar a resposta
        estacoes = [j+1 for j in range(regioes)]
        id_excluir = 0

        while len(estacoes) > 1:

            # Caso o ID_EXCLUIR for maior que o vetor, pegue a parte que
            # ultrapassou (resto da divisao) e coloque no inicio do vetor
            if id_excluir > len(estacoes)-1:
                id_excluir = id_excluir % len(estacoes)

            # Cuidado com POP, pois ele exibe na tela o elemento retirado
            estacoes.pop(id_excluir)

            # Eliminou o ultimo, entao, ID_EXCLUIR > tamanho do vetor
            # O proximo a iniciar a contagem é o elemento da frente,
            # ou seja, com indice ZERO
            if id_excluir > len(estacoes) - 1:
                id_excluir = 0

            # Adequacao para considerar na contagem tb o elemento atual
            id_excluir += salto-1

        if estacoes[0] == 13:
            print(salto)
            break