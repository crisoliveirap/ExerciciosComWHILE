# Estatíticas em produtos
total1000 = 0
total = 0
menor = 0
cont = 0
produto = ''
while True:
    print('LOJA SUPER BARATÃO')
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        total1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi {total:.2f}.')
print(f'Ao todo temos {total1000} produtos custando mais de mil reais.')
print(f'O produto mais barato foi {barato} que custou R${menor:.2f}')