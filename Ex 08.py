# Maior e menor valores
resp = 'S'
cont = 0
soma = 0
media = 0
while resp == 'S':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    cont += 1
    soma += num
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}.')