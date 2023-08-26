import os
os.system('cls')
print('\033[1;92m' + '='*45)
nome = input('Digite sua nome: ')
idade = int(input('Digite sua idade: '))
if(idade > 17):
    print(f'{nome} eh maior de idade!')
else:
    print(f'{nome} eh menor de idade!')
    
    