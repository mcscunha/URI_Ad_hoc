#!/usr/bin/env python3
# -*- coding: utf-8 -*-

linhas = input().split()
pilhas = int(linhas[0])
transp_max = int(linhas[1])

linhas = list(map(int, input().split()))
dali_inicia = True
while len(linhas):
    linhas[0] -= transp_max
    if linhas[0] <= 0:
        del(linhas[0])
    dali_inicia = not dali_inicia

print('Dila' if dali_inicia else 'Dali')
