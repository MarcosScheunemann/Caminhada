"""
# Ajuda interativa

help(quit)
print(input.__doc__)



# como criar um menu da ajuda atravez da função que criou:
def contador(i=0, f=0, p=0):  #deixar o "=0" faz com que o paramentro seja opcional e não cenessário
    """
    #-> Faz uma contagem e mostra na tela
    #:param i: inicio da contagem
    #:param f: fim da contagem
    #:param p: passo da contagem
    #:return: sem retorno
    """
    global a   #o global puxa uma informação do global e inporta na função e faz com que a função altere o valor global
    c = i
    while c <= f:
        print(f'{c}', end=" ")
        c += p
    print("FIM!")


a = 2
contador(1, 3, 1)
help(contador)


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  #devolve o valor ao resultado da função


r1 = somar(3, 2, 5)
r2 = somar(1, 7)

print(f'Meus cálculos deram {r1} e {r2}')


#ex1:
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n= int(input('Digite um número: '))
print(f'o Fatorial de {n} é igual a {fatorial(n)}')

#ex1:
def par(n=0)
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par"')

    
"""

print("=-"*30)
print('exercicio 1')

from datetime import date
anoatual = date.today().year


def voto(n):
    global anoatual
    global idade
    if 18 <= idade <= 65:
        return "OBRIGATÓRIO"
    if 16 <= idade < 18 or idade >= 65:
        return "OPICIONAL"
    if idade < 16:
        return "NEGADO"


print('Descubra se pode votar! ')
ano = int(input("Ano de nascimento: "))
idade = anoatual - ano
print(f'Você tem {idade} anos e o voto é {voto(ano)}')

print("=-" * 30)
print('exercicio 2')


def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicional) Mostrar ou não mostrar a conta.
    :return: O resultado do fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c == 1:
                print(f' {c}', end=" = ")
            else:
                print(f' {c}', end=" x")
    return f


print(fatorial(10, True))

help(fatorial)

print("=-" * 30)
print('exercicio 3')


def ficha(nome, gols):
    if nome.strip() == "":
        nome = '<Desconhecido>'
    if gols == "":
        gols = 0
    elif gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


jogador = str(input('Digite o nome do jogador: '))
Gols = str(input('Digite o número de gols: '))

ficha(jogador, Gols)

print("=-" * 30)
print('exercicio 4 ou 104')


def leiaint(n):
    algo = input(n)
    while not algo.isnumeric():
        print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m') #colocando na cor vermelho.
        algo = input(n)

    return algo


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')

print("=-" * 30)
print('exercicio 5')


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param sit: Valor opicional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    T = len(n)
    M = max(n)
    N = min(n)
    Med = sum(n) / len(n)
    if Med <= 5:
        Situ = 'RUIM'
    elif 5 < Med <= 7:
        Situ = 'RAZOÁVEL'
    elif 7 < Med <= 10:
        Situ = 'BOA'
    else:
        Situ = 'Inválido'

    if not sit:
        return {'Total': T, 'Maior': M, 'Menor': N, 'Média': Med}
    if sit:
        return {'Total': T, 'Maior': M, 'Menor': N, 'Média': Med, 'Situação': Situ}


resp = notas(9, 10, 8, 4.5, 3.7, sit=True)
print(resp)

print("=-" * 30)
print('exercicio 6')
c = ('\033[m',         # 0 - sem cores
     '\033[0;30;41m',  # 1 - Vermelho
     '\033[0;30;42m',  # 2 - Verde
     '\033[0;30;43m',  # 3 - Amarelo
     '\033[0;30;44m',  # 4 - Azul
     '\033[0;30;45m',  # 5 - Roxo
     '\033[7;30m',     # 6 - Branco
     )


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f'  {msg}')
    print("~" * tam)
    print(c[0], end='')


H = 0

while True:
    título('SISTEMA DE AJUDA PyHELP',2)
    H = input("Função ou Biblioteca > ")
    if H.upper() == 'FIM':
        break
    título(f"Acessando o comando '{H}'", 4)
    help(H)
título('ATÉ LOGO', 1)
