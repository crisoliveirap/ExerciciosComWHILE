# Ex 01: Validação de dados
sexo = str(input('Informe seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    mensagem = str(input('Dados inválidos! Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')