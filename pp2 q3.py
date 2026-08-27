ct = 0
ct1 = 0
ct2 = 0
soma = 0
ct_par = 0
ct_imp = 0
valor1 = 0
valor2 = 0
while True:
    valor = int(input('Digite um valor: '))
    if valor == 0:
        break
    ct = ct + 1
    soma = soma + valor
    if valor % 2 == 0:
        ct1 = ct1 + 1
        valor1 = valor1 + valor
    if valor % 2 == 1:
        ct2 = ct2 + 1
        valor2 = valor2 + valor
print('Quantidade total de numeros:', ct)
print('Soma total dos numeros:', soma)
print('Media dos numeros pares:', valor1/ct1)
print('Media dos numeros impares:', valor2/ct2)