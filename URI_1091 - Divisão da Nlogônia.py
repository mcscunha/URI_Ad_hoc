# -*- coding: utf-8 -*-

'''
            |
       NO   |   NE
            |
    ------- 0 --------
            |
       SO   |   SE
            |

'''
while True:
    consultas = int(input())
    
    if consultas == 0:
        break

    zero_x, zero_y = list(map(int, input().split(' ')))
    for caso in range(consultas):
        x, y = list(map(int, input().split(' ')))

        # Em cima de qualquer linha divisoria
        if (x == zero_x) or (y == zero_y):
            print('divisa')
        elif (x < zero_x):
            print('NO' if y > zero_y else 'SO')
        else:
            print('NE' if y > zero_y else 'SE')
