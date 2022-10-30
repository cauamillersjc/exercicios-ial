def calcH(n):
    num = 1
    h = 1
    isSum = True

    while num < n:
        num += 1

        if isSum:
            h += (num * 2 - 1) / num
            isSum = False
        else:
            h -= (num * 2 - 1) / num
            isSum = True
    
    return h

def calcS(n):
    num = 1
    s = 1
    isSum = False

    while num < n:
        num += 1

        if isSum:
            s += num / (num * num)
            isSum = False
        else:
            s -= num / (num * num)
            isSum = True
    
    return s

def calcP(n):
    numA = 2
    numB = 1
    p = 0

    for x in range(n):
        p += numA / numB ** 3

        numB += 2

        count = 1

        while True:
            if checkPrimeNumber(numA + count):
                numA += count
                break
                
            count += 1

    return p


def checkPrimeNumber(num):
    isPrimeNumber = True

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                isPrimeNumber = False
                break

    if isPrimeNumber:
        return True
    else:
        return False

#################################

numH = int(input("Digite o valor para H. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

while numH < 50 or numH < 0:
    numH = int(input("Digite o valor para H. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

totalH = calcH(numH)

print(f"\nH é igual a: {totalH}\n")

#################################

numS = int(input("Digite o valor para S. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

while numS < 50 or numS < 0:
    numS = int(input("Digite o valor para S. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

totalS = calcS(numS)

print(f"\nS é igual a: {totalS}\n")

#################################

numP = int(input("Digite o valor para P. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

while numP < 50 or numP < 0:
    numP = int(input("Digite o valor para P. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

totalP = calcP(numP)

print(f"\nP é igual a: {totalP}\n")

#################################