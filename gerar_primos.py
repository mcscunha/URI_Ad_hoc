from math import sqrt, ceil


def checkPrime(num, baseList):    
    for p in baseList:
        if (p > ceil(sqrt(num))): 
            break

        if num % p == 0:
            return False
    return True

def primes(q):
    primelist, number = [2], 3

    while len(primelist) < q:
        if checkPrime(number, primelist):
            primelist.append(number)
        number += 2
    return primelist

def main(qtde):
    lista = primes(qtde)
    print("Saída:\n", lista)
    #print("Saída: ", [lista[i] for i in [qtde-1, 1, 7]])


if __name__ == '__main__':
    main(3510)
