# -*- coding: utf-8 -*-

matriz = {
    'C': [0, 0, 0],
    'Q': [0, 0, 0],
    'T': [0, 0, 0],
}

while True:
    cartas = int(input())
    
    if cartas == 0:
        break

    numero_sets = 0
    c1, c2, c3 = False, False, False
    q1, q2, q3 = False, False, False
    t1, t2, t3 = False, False, False
    for carta in range(cartas):
        n, s = input().split(' ')
        if s[0] == 'c':
            if n[0] == 'u':
                matriz['C'][0] += 1
                c1 = True
                if matriz['C'][0] == 3:
                    numero_sets += 1
                    matriz['C'][0] -= 3
                    c1 = False
            elif n[0] == 'd':
                matriz['C'][1] += 1
                c2 = True
                if matriz['C'][1] == 3:
                    numero_sets += 1
                    matriz['C'][1] -= 3
                    c2 = False
            elif n[0] == 't':
                matriz['C'][2] += 1
                c3 = True
                if matriz['C'][2] == 3:
                    numero_sets += 1
                    matriz['C'][2] -= 3
                    c3 = False
            
        elif s[0] == 'q':
            if n[0] == 'u':
                matriz['Q'][0] += 1
                q1 = True
                if matriz['Q'][0] == 3:
                    numero_sets += 1
                    matriz['Q'][0] -= 3
                    q1 = False
            elif n[0] == 'd':
                matriz['Q'][1] += 1
                q2 = True
                if matriz['Q'][1] == 3:
                    numero_sets += 1
                    matriz['Q'][1] -= 3
                    q2 = False
            elif n[0] == 't': 
                matriz['Q'][2] += 1
                q3 = True
                if matriz['Q'][2] == 3:
                    numero_sets += 1
                    matriz['Q'][2] -= 3
                    q3 = False
        elif s[0] == 't':
            if n[0] == 'u':
                matriz['T'][0] += 1
                t1 = True
                if matriz['T'][0] == 3:
                    numero_sets += 1
                    matriz['T'][0] -= 3
                    t1 = False
            elif n[0] == 'd':
                matriz['T'][1] += 1
                t2 = True
                if matriz['T'][1] == 3:
                    numero_sets += 1
                    matriz['T'][1] -= 3
                    t2 = False
            elif n[0] == 't':
                matriz['T'][2] += 1
                t3 = True
                if matriz['T'][2] == 3:
                    numero_sets += 1
                    matriz['T'][2] -= 3
                    t3 = False

        # Mesmo simbolo
        if c1 and c2 and c3:
            matriz['C'][0] -= 1
            matriz['C'][1] -= 1
            matriz['C'][2] -= 1
            c1, c2, c3 = False, False, False
            numero_sets += 1
        elif q1 and q2 and q3:
            matriz['Q'][0] -= 1
            matriz['Q'][1] -= 1
            matriz['Q'][2] -= 1
            q1, q2, q3 = False, False, False
            numero_sets += 1
        elif t1 and t2 and t3:
            matriz['T'][0] -= 1
            matriz['T'][1] -= 1
            matriz['T'][2] -= 1
            t1, t2, t3 = False, False, False
            numero_sets += 1

        # Simbolos diferentes
        if matriz['C'][0] and matriz['Q'][1] and matriz['T'][2]:
            matriz['C'][0] -= 1
            matriz['Q'][1] -= 1
            matriz['T'][2] -= 1
            numero_sets += 1
        elif matriz['C'][0] and matriz['Q'][2] and matriz['T'][1]:
            matriz['C'][0] -= 1
            matriz['Q'][2] -= 1
            matriz['T'][1] -= 1
            numero_sets += 1
        elif matriz['C'][1] and matriz['Q'][2] and matriz['T'][0]:
            matriz['C'][1] -= 1
            matriz['Q'][2] -= 1
            matriz['T'][0] -= 1
            numero_sets += 1
        elif matriz['C'][1] and matriz['Q'][0] and matriz['T'][2]:
            matriz['C'][1] -= 1
            matriz['Q'][0] -= 1
            matriz['T'][2] -= 1
            numero_sets += 1
        elif matriz['C'][2] and matriz['Q'][0] and matriz['T'][1]:
            matriz['C'][2] -= 1
            matriz['Q'][0] -= 1
            matriz['T'][1] -= 1
            numero_sets += 1
        elif matriz['C'][2] and matriz['Q'][1] and matriz['T'][0]:
            matriz['C'][2] -= 1
            matriz['Q'][1] -= 1
            matriz['T'][0] -= 1
            numero_sets += 1

    print(numero_sets)
