import os
os.system('cls')
print('\033[1;92m' + '='*45)
nome = input('Digite sua nome: ')
salario = float(input('Digite o seu salario: '))
print(f'O nome ganha de salario {salario}')
print('O {0} ganha de salario {1}' .format(nome, salario))
#calculo de descontos de salario
if(salario <= 1320):
    print('Nao há descontos')
else:
    desconto = (salario * 27/100) 
    print('O desconto do salario é de {1} do salario de {0}! ' .format(salario, desconto))