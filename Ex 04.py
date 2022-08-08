# Ex 04: Progressão Aritmética
print('Gerador de PA')
print('-=' * 10)
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 1
while cont <= 10:
    print(f'{termo}', end=' → ')
    termo += razao
    cont += 1
print('FIM')