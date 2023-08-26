#importar pacote do so
import os
#limpar tela
os.system('cls')
#comando de repetir o caractere e muda cor da escrita do terminal
print('\033[1;92m' + '='*45)
print('\033[1;92m' + ' '*10 + 'Exercicio 2' + ' '*10)

nome = input('Digite seu nome: ')
print('Vc digitou: ' + nome)
print('sua idade eh: ' + input('Digite sua idade: '))
print(f'O {nome} eh o nome do individuo! ')
idade = input('digite a idade: ')
#print('Viveu ' + int(idade) * 365 + 'dias de vida!')