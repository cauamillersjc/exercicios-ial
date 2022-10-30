ascCountSeq = 1
ascBigSeq = 1
equalCountSeq = 1
equalBigSeq = 1
lastNumber = 0

for x in range(150):
    number = int(input(f"Digite o {x + 1}º número: "))
    if x != 0:
        if number > lastNumber:
            ascCountSeq += 1
            if ascCountSeq > ascBigSeq:
                ascBigSeq = ascCountSeq
        elif number == lastNumber:
            equalCountSeq += 1
            if equalCountSeq > equalBigSeq:
                equalBigSeq = equalCountSeq
    lastNumber = number

print(f"O tamanho da maior sequência crescente é: {ascBigSeq}")
print(f"O tamanho da maior sequência constante é: {equalBigSeq}")