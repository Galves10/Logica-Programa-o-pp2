apr = 0
rep = 0
ct = 0
soma = 0
while True:
    notas = float(input('Digite a nota do aluno: '))
    if notas == -1:
        break
    ct = ct + 1
    soma = soma + notas
    if notas >= 5:
        apr = apr + 1
    if notas < 5:
        rep = rep + 1
print('Quantidade de alunos:', ct)
print('Quantidade de alunos aprovados', apr)
print('Quantidade de alunos reprovados', rep)
print('Media da turma:', soma/ct)