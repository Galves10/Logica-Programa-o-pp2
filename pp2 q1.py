ct = 0
qt = 0
soma = 0
while True:
    valor = float(input('Digite um valor: '))
    if valor == 0.5:
        break
    ct = ct + 1
    soma = soma + valor
    if valor > 20:
        qt = qt + 1

print('Quantidade de valores:', ct)
print('Soma dos valores:', soma)
print(f'Media {soma / ct:.2f}')
print('Quantidade de valores maiores que 20:', qt)