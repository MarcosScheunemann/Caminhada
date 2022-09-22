"""
colocando listas dentro de listas:

pessoas = []
p1 = ['Pedro', 25]
p2 = ['Maria', 19]

pessoas.append(p1[:])
print(pessoas)
pessoas.append(p2[:])
print(pessoas[0][0][0])

ex 1:

teste = list()
teste.append('Gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

ex2:
# usando estrutura composta para localizar dados
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13]]
print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

galera = []
dado = []
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
menores = maiores = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        maiores += 1
    else:
        print(f'{p[0]} é menor de idade')
        menores += 1
print(f'Temos {maiores} maiores e {menores} menores de idade.')

"""
print('-=-=-'*20)

print('exercicio 1')
galera = []
pessoas = []

while True:
    pessoas.append(str(input("Nome: ")))
    pessoas.append(float(input('Peso: ')))
    galera.append(pessoas[:])
    pessoas.clear()
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input('Quer continuar?[S/N]: ')).upper()
    if continuar == 'N':
        break

print(f'Ao todo você cadastrou {len(galera)} pessoas.')

maiorpeso = menorpeso = 0
for p in galera:
    if p[1] >= maiorpeso:
        maiorpeso = p[1]
    elif menorpeso == 0:
        menorpeso = p[1]
    elif p[1] <= menorpeso:
        menorpeso = p[1]

print(f'O maior peso foi de {maiorpeso} Kg. Peso de ', end="")
for p in galera:
    if maiorpeso == p[1]:
        print(f'{p[0]}', end=" ")
print()

print(f'O menor peso foi de {menorpeso} Kg. Peso de ', end="")
for p in galera:
    if menorpeso == p[1]:
        print(f'{p[0]}', end=" ")
print()

print('-=-=-'*20)
print('exercicio 2')

pares = []
impares = []
n = [pares, impares]

cont = 0
while True:
    cont += 1
    num = int(input(f"Digite o {cont}° valor: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    if cont == 7:
        break
impares.sort()
pares.sort()

print(f'Os valores pares digitados foram: {n[0]}')
print(f'Os valores impares digitados foram: {n[1]}')

print('-=-=-'*20)
print('exercicio 3')

linha1 = []
linha2 = []
linha3 = []
matrix = [linha1, linha2, linha3]

for lin in range(0, 3):
    for c in range(0, 3):
        if lin == 0:
            linha1.append(int(input(f'Digite um valor para [{lin}, {c}]: ')))
        elif lin == 1:
            linha2.append(int(input(f'Digite um valor para [{lin}, {c}]: ')))
        elif lin == 2:
            linha3.append(int(input(f'Digite um valor para [{lin}, {c}]: ')))

print(f'''
[{matrix[0][0]}][{matrix[0][1]}][{matrix[0][2]}]
[{matrix[1][0]}][{matrix[1][1]}][{matrix[1][2]}]
[{matrix[2][0]}][{matrix[2][1]}][{matrix[2][2]}]
''')

print('-=-=-'*20)
print('exercicio 4')

linha1 = []
linha2 = []
linha3 = []
matrix = [linha1, linha2, linha3]

for lin in range(0, 3):
    for c in range(0, 3):
        if lin == 0:
            linha1.append(int(input(f'Digite um valor para [{lin}, {c}]: ')))
        elif lin == 1:
            linha2.append(int(input(f'Digite um valor para [{lin}, {c}]: ')))
        elif lin == 2:
            linha3.append(int(input(f'Digite um valor para [{lin}, {c}]: ')))

print(f'''
[{matrix[0][0]}][{matrix[0][1]}][{matrix[0][2]}]
[{matrix[1][0]}][{matrix[1][1]}][{matrix[1][2]}]
[{matrix[2][0]}][{matrix[2][1]}][{matrix[2][2]}]
''')

pares = 0
for lin in range(0, 3):
    for c in range(0, 3):
        if matrix[lin][c] % 2 == 0:
            pares += matrix[lin][c]
soma = 0
for num in range(0, 3):
    soma += matrix[num][2]

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior da segunda linha é {max(matrix[1])}.')

print('-=-=-'*20)
print('exercicio 5')

from random import randint

total = []
jogos = int(input("Quantos jogos quer que sorteie? "))
lista = []
cont = 0
cont1 = 0
while True:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont1 += 1
        if cont1 == 6:
            lista.sort()
            total.append(lista[:])
            lista.clear()
            break
    cont += 1
    cont1 = 0
    if cont == jogos:
        break

for c, v in enumerate(total):
    print(f'Jogo {c + 1}: {total[c]}')

print('-=-=-'*20)
print('exercicio 6')

notas = []
aluno = []
geral = []

while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(notas[:])
    notas.clear()
    geral.append(aluno[:])
    aluno.clear()
    continuar = " "
    while continuar not in "SsNn":
        continuar = str(input("Quer coninuar?[S/N] ")).upper()
    if continuar == "N":
        break

print('-=' * 30)
print(f'No. NOME                     MÉDIA')
print('-' * 50)
for c, v in enumerate(geral):
    print(f'{c}  {geral[c][0]:20}     {(geral[c][1][0] + geral[c][1][1]) / 2:6}')

while True:
    a = int(input('Mostrar notas de qual aluno?(999 interrompe) : '))

    if a <= len(geral):
        print(f'Notas de {geral[a][0]} são {geral[a][1]}')

    if a == 999:
        print('FINALIZANDO...')
        break
