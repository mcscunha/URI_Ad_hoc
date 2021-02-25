# -*- coding: utf-8 -*-


from collections import deque


# Ler o conteudo do arquivo de valores e guardar em uma LISTA de LISTA STR
def read_line_txt(arquivo_txt):
    import os
    with open(file=arquivo_txt, mode='r', encoding='utf8', newline='\n') as f:
        linhas = []
        while True:
            linha = f.readline()
            if not linha:
                break 
            linhas.append(linha.strip().split(' '))
    return linhas


#
# Solução desenvolvida por: 
#
def jos(k, j):
    d = deque(k)
    while len(d) > 1:
        d.rotate(-j)
        d.pop()
    breakpoint()
    return(d.pop())


linhas = read_line_txt('1030_valores.txt')
for i in range(int(linhas[0][0])):
    k, j = linhas[i+1]
    k = [x for x in range(1, int(k)+1)]
    j = int(j)
    result = jos(k, j)
    print('Case %d: %d'%(i+1, result))