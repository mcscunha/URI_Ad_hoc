# -*- coding: utf-8 -*-

def read_line_txt():
    import os
    with open('valores.txt', 'r') as f:
        return f.readlines()

def read_integer():
    return int(input())

def read_line_int_com_espacos():
    return [ int(i) for i in input().split() ]
    #return list(map(int, input().split()))
    #return input().split(' ')

def int_to_32bits(inteiro):
    return f'{ bin(inteiro)[2:]:0>32 }'
    #return f'{inteiro:032b}'

def int_to_nbits(inteiro, bits):
    '''Converte um inteiro em um binario de n bits'''
    return f'{ bin(inteiro)[2:] }'.zfill(bits)

def int_to_8bits(inteiro):
    '''Converte um inteiro em um binario de 8 bits'''
    return f'{ inteiro:08b }'

def bin_to_int(binario):
    '''Converte binario str em inteiro'''
    return int(binario, 2)


while True:
    try:
        lista = read_line_int_com_espacos()
        lista = sorted(lista, reverse=True)
        bits = len(bin(lista[0])[2:])
        bit_a = int_to_nbits(lista[0], bits)
        bit_b = int_to_nbits(lista[1], bits)
        
        #print(bit_a, ' - ', bit_b)
        soma = ''
        for i in range(bits):
            # if bit_a[i] == bit_b[i]:
            #     soma += '0'
            # else:
            #     soma += '1'
            soma += '1' if bit_a[i] or bit_b[i] else '0'
        print(soma) 
    except EOFError:
        break
