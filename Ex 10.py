# Tabuada
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    print('-=-'*10)
    if num < 0:
        break
    else:
        for c in range (1, 11):
            print(f'{num} x {c:2} = {num * c:2}')
        print('-=-' * 10)
print('Programa tabuada encerrado! Volte sempre!')