# -*- coding: utf-8 -*-

while True:
    try:
        linha = input()
        lista = [abs(int(i)) for i in linha.split(' ')]
        print(int(bin(lista[0] ^ lista[1]), 2)) 
    except EOFError:
        break
