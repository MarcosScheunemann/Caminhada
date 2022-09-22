"""
from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)

print(f'O fatorial de {num} é {fat}.')
print(f'O dobro de {num} é {numeros.dobro(num)}')
"""

print("=-" * 30)
print('exercicio 1')

from uteis import desafio107
from uteis import dados

p = float(input('Digite o preço: R$'))
print(f'A metade de {desafio107.moeda(p)} é {desafio107.metade(p, True)}')
print(f'O dobro de {desafio107.moeda(p)} é {desafio107.dobro(p, True)}')

a = float(input('O quanto quer aumentar? % '))
d = float(input('Q quanto que diminuir? % '))

print(f'Aumentando {a}%, temos {desafio107.aumentar(p, a, True)}')
print(f'Diminuindo {d}%, temos {desafio107.diminuir(p, d, True)}')

print("=-" * 30)
print('exercicio 2')

print(desafio107.moeda(30.36))

print("=-" * 30)
print('exercicio 3')

print(desafio107.metade(10, True))

print("=-" * 30)
print('exercicio 4')

p = dados.leiaDinheiro('Digite um preço R$: ')
a = float(input('Quanto quer aumentar? %'))
d = float(input('Quanto quer diminuir? %'))

desafio107.resumo(p, a, d)

print("=-" * 30)
print('exercicio 5')

print('feito')

print("=-" * 30)
print('exercicio 6')

print('feito')
