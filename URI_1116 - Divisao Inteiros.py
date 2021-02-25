# -*- coding: utf-8 -*-
n = int(input())
for vezes in range(n):

    try:
        x, y = map(int, input().split())
        result = x / y
        print(f'{result:.1f}')
    except:
        print('divisao impossivel')
