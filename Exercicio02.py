sf = int (input("Informe qual é o salario: "))
total = 0
continuar = 's'
vendas = 0



while (continuar == 's'):
    vendas += float(input('Insira suas vendas: '))
    continuar = input('Digite "s" se quiser continuar: ')

if sf <= 1500:
    total = sf + (vendas*0.05)

if sf > 1500:
    total = sf + (vendas*0.05) + ((vendas-1500)*0.07)


print(f'Salário final {total}')

