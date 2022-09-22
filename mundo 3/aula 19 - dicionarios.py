"""
Dicionários personaliza os indices.
ex1:
dados = {'nome': 'Pedro', 'idade': 25}

print(dados['nome'])

# adicionar elementos.
dados['sexo'] = 'M'

del dados['idade']

print(dados.values())
print(dados.keys())
print(dados.items())

for k, v in dados.items():
    print(f'o {k} é {v}')

ex2:
estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    print(e)
    for v in e.values():
        print(v, end=" ")
    print()

"""
print('exercicio 1')

aluno = {'nome': str(input('Nome: '))}
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    passou = "Aprovado"
else:
    passou = "Reprovado"

print(f'Situação é igual a {passou}')

print("*--*-*-"*15)
print('exercicio 2')

from random import randint
from time import sleep
from operator import itemgetter

jogadas = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = []
print('Valores sorteados: ')
for c, v in jogadas.items():
    sleep(0.50)
    print(f'O {c} tirou {v}')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)

print("-="*20)
print('Ranking dos jogadores:')

for i, v in enumerate(ranking):
    print(f'{v[0]} tirando {v[1]} ficou em {i+1}° lugar')
    sleep(0.5)

print("*--*-*-"*15)
print('exercicio 3')
# 35 anos de contribuinte para aposentar

from datetime import date

anoatual = date.today().year

pessoa = {'Nome': str(input('Nome: ')),
          'Idade': anoatual - int(input('Ano de nascimento: ')),
          'ctps': int(input('Carteira de Trabalho (0 não tem): '))}

if pessoa['ctps'] == 0:
    for c, v in pessoa.items():
        print(f'{c} tem o valor {v}')
else:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Aposentadoria'] = ((pessoa['Contratação'] + 35) - anoatual) + pessoa['Idade']

    for c, v in pessoa.items():
        print(f'{c} tem o valor {v}')

print("*--*-*-"*15)
print('exercicio 4')

jogador = {'nome': str(input('Nome do jogador: '))}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
Gols = []

for c in range(0, partidas):
    Gol = int(input(f'Quantos gols na partida {c+1}? '))
    Gols.append(Gol)

jogador['gols'] = Gols[:]
jogador['total'] = sum(Gols)

print('-='*30)
print(jogador)
print('-='*30)

for d, f in jogador.items():
    print(f'O campo {d} tem o valor {f}.')
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for u in range(0, partidas):
    print(f'    => Na partida {u+1}, fez {Gols[u]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

print("*--*-*-" * 15)
print('exercicio 5')

lista = []
while True:
    pessoa = {'Nome': str(input("Nome: ").title()),
              'Sexo': str(input('Sexo: [M/F] ')).upper(),
              'idade': int(input('Idade: '))}
    lista.append(pessoa.copy())
    del pessoa

    continuar = " "
    while continuar not in "NnSs":
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == "N":
        break

print(f'O grupo tem {len(lista)} pessoas.')

idades = []
for c, v in enumerate(lista):
    idades.append(v["idade"])

idademedia = sum(idades) / len(lista)
print(f'- A média de idade é de {idademedia:.2f} anos.')

print('As mulheres cadastradas foram: ', end="")

for c, v in enumerate(lista):
    if v['Sexo'] == "F":
        print(v['Nome'].title(), end=" ")
print()

print('lista de pessoas que estão acima da média:')
print()
for c, v in enumerate(lista):
    if v['idade'] > idademedia:
        for f, x in v.items():
            print(f'{f} = {x}', end="; ")
        print()
        print()

print('<< ENCERRADO >>')

print("*--*-*-" * 15)
print('exercicio 6')

lista = []
while True:
    jogador = {'nome': str(input('Nome do jogador: ')).title()}
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    Gols = []

    for c in range(0, partidas):
        Gol = int(input(f'Quantos gols na partida {c+1}? '))
        Gols.append(Gol)

    jogador['gols'] = Gols[:]
    jogador['total'] = sum(Gols)

    lista.append(jogador.copy())

    del jogador

    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("quer continuar? [S/N] ")).upper()
    if continuar == "N":
        break
print('-='*30)
print(f'cod nome            gols              total')
print('--------------------------------------------')
for c, v in enumerate(lista):
    print(c, end=" ")
    print(f'{v["nome"].title():15}', end="")
    print(f'{str(v["gols"]):20}', end="")
    print(f'{v["total"]:4}')
print('--------------------------------------------')

dado = 0
while dado != 999:
    dado = int(input('Mostrar dados de qual jogador? '))
    if dado == 999:
        break
    elif dado < 0 or dado >= len(lista):
        print(f'ERRO! Não existe jogador com código {dado}! Tente novamente')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {lista[dado]["nome"]}:')
        for u, g in enumerate(lista):
            if u == dado:
                for h, j in enumerate(g["gols"]):
                    print(f'    => Na partida {h+1}, fez {j} gols.')
print('Volte sempre.')
