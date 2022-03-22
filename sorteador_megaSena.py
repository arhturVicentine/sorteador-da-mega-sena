from random import randint
from time import sleep
print('=-' * 20)
print(f'{"SORTEANDO NÚMEROS PARA A MEGA SENA" :^40}')
print('=-' * 20)
lista = []
sorteio= []
quantidade = int(input('Quantos jogos deseja sortear? '))
total = 1
while total <= quantidade:
    contador = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            contador += 1
        if contador >=6:
            break
    lista.sort()
    sorteio.append(lista[:])
    lista.clear()
    total += 1
print('=-' * 3,f'SORTEANDO {quantidade} jogos', '=-' * 3)
sleep(1)
for indice,linha in enumerate(sorteio):
    sleep(1)
    print(f'Jogo {indice+1} : {linha}')

print('BOA SORTE!!!')






