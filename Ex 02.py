# Ex 02: Criando um menu de opções
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while True:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] escolher novos valores
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é sua opção? '))
    print('-=-' * 10)
    if opcao == 1:
        soma = num1 + num2
        print(f'A soma entre {num1} e {num2} é {soma}.')
    elif opcao == 2:
        multiplica = num1 * num2
        print(f'O resultado de {num1} x {num2} é {multiplica}.')
    elif opcao == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2}, o maior é {num1}.')
        elif num1 < num2:
            print(f'Entre {num1} e {num2}, o maior é {num2}.')
        elif num1 == num2:
            print(f'Os valores são iguais.')
    elif opcao == 4:
        print('Informe os valores novamente: ')
        num1 = int(input('Primeiro valor:'))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Fim do programa! Volte sempre!')
        break
    else:
        print('Opção inválida! Digite uma opção: ')
    print('-=-' * 10)
    sleep(2)