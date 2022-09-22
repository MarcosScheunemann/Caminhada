"""
Exemplo teórico:

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:                          => início da condicional
    print('Carro novo')                 => tudo que estiver endentado está no bloco verdadeiro
else:
    print('Carro velho')                => tudo que estiver endentado aqui, é o bloco falso
print('--FIM--')                        => execução do final

execução simplificada:

tempo = int(input('Quantos anos tem seu carro?'))
print('Carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

Exemplo 2 :

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n = (n1 + n2)/2
print('Sua média é {}'.format(n))
if n >= 6.0:
    print('Que nota boa!')
else:
    print('Que merda de nota!')

"""

from random import randint

NC = int(randint(0, 5))   # faz o computador pensar em um aleatório entre dois número inteiros
NP = int(input('Escolha um número de 0 a 5: '))
if NC == NP:
    print('PARABÉNS, você acertou o número escolhido!')
else:
    print('Que pena! Você errou, o número era {}'.format(NC))

print('-=-' * 20)

VC = float(input('Qual a velocidade ultrapassada em KM/H?: '))
if VC > 80:
    VM = float((VC-80)*7)
    print('Multa! o valor da multa é R${:.2f} reais'.format(VM))
else:
    print('Sem multa.')

print('-=-' * 20)

Num = int(input('Digite um número: '))
if Num % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar')

print('-=-' * 20)

Km = float(input('Digite a distância de sua viagem em KM: '))
if Km <= 200:
    Preco = Km * 0.50
    print('O preço da passagem é {:.2f} reais'.format(Preco))
else:
    Preco = Km * 0.45
    print('O preço da passagem será de {:.2f} reais'.format(Preco))

print('-=-' * 20)

from datetime import date
BX = int(input('Digite um ano para ver se é um ano bissexto: '))
if BX == 0:
    BX = date.today().year
if BX % 4 == 0 and BX % 100 != 0 or BX % 400 == 0:   # != significa "DIFERENTE DE "
    print('Este ano é um ano Bissexto.')
else:
    print('Não é um nao bissexto.')

print('-=-' * 20)

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite o terceiro número: '))
min = min([numero1, numero2, numero3])
max = max([numero1, numero2, numero3])
print('O menor número é {:.2f} e o maior número é {:.2f}.'.format(min, max))

print('-=-' * 20)

Sal = float(input('Qual o salário do funcionário? '))
if Sal > 1250:
    Salf = Sal * 1.10
else:
    Salf = Sal * 1.15
print('O salário ficará em {:.2f} reais com o aumento.'.format(Salf))

print('-=-' * 20)

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('Essas três retas podem formar um triangulo.')
else:
    print('Essas três retas não podem formar um triangulo.')
