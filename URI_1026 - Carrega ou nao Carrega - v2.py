# -*- coding: utf-8 -*-

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


linhas = read_line_txt('1026_valores.txt')

#
# Usando FOR para manipular os dados
#
for linha in linhas:
    
    # Comparacao bit a bit (XOR) de integer. Igual a 1 somente se 1 E 1
    bits = int(linha[0]) ^ int(linha[1]) 
    
    print(bits)

print('-' * 48)


#
# Usando WHILE para manipular os dados
#
i = 0
while True:
    try:
        linha = linhas[i]
        i += 1
        
        print(int(linha[0]) ^ int(linha[1]))
    except IndexError:
        break

print('-' * 48)
