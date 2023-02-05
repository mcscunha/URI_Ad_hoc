#!/usr/bin/env python3
# -*- coding: utf-8 -*-

linhas = input().split()
pilhas = int(linhas[0])
transp_max = int(linhas[1])

linhas = list(map(int, input().split()))

'''
## Sem sucesso
dali_inicia = True
pilha = 0
while pilha < pilhas:
    linhas[pilha] -= transp_max
    if linhas[pilha] <= 0:
        pilha += 1
    dali_inicia = not dali_inicia
print('Dila' if dali_inicia else 'Dali')
'''

## Sem sucesso
total_brinq = sum(linhas)
vezes = total_brinq // transp_max
resto = total_brinq % transp_max
if resto:
    print('Dila' if (vezes+1) % 2 == 0 else 'Dali')
else:
    print('Dila' if vezes % 2 == 0 else 'Dali')