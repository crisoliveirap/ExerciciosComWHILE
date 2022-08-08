# Vários números com flag
cont = 0
soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))