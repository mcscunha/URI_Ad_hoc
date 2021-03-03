# -*- coding: utf-8 -*-

while True:
    xi, yi, xf, yf = list(map(int, input().split(' ')))

    # Codigo de parada
    if (xi + yi + xf + yf) == 0:
        break
    
    # Nao houve movimento. A dama ficou no mesmo lugar
    if (xi == xf) and (yi == yf):
        print(0)
    
    # Movimentacao na mesma coluna
    # Movimentacao na mesma linha
    # Se diferenca entre origem e destino sao iguais em X e Y, entao, diagonal
    elif (xi == xf) or (yi == yf) or abs(xi - xf) == abs(yi - yf):
        print(1)
    
    # Todos os outros lugares do tabuleiro, a dama alcanca em dois movimentos
    else:
        print(2)