"""
Aula 15
ex 1 :
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma total é {s}.')

"""
s = cont = 0
while True:
    n = int(input('Digite um número para a soma final (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'A soma dos {cont} números é {s}.')

print("-=" * 40)

while True:
    n = int(input('Digite um núemro para ver a Tabuada: '))
    if n < 0:
        print('Tudo bem, chega.')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print("--**--" * 20)

print("-=" * 40)

from random import randint

cont = 0
while True:
    comp = randint(0, 11)
    n = int(input('Digite um núemro para jogar: '))
    r = str(input('Digite o resultado da soma [P/I]: ')).upper().strip()
    soma = comp + n

    if soma % 2 == 0:
        result = "P"
    else:
        result = "I"

    if result == r:
        print(f'O computador jogou {comp}, Você ganhou!')
        cont += 1
    elif result != r:
        print(f'O computador jogou {comp}, você perdeu, mas conseguiu {cont} vitórias consecutivas.')
        break
    print("--**--" * 20)

print("-=" * 40)

contadultos = conthomem = contnovinhas = 0
while True:
    idade = (input('Qual a idade? '))
    while not idade.isnumeric():
        idade = (input('Qual a idade? '))
    idade = int(idade)

    sexo = str(input('Qual o seu sexo[M/F]? ')).upper().strip()
    while sexo not in "FM":
        sexo = str(input('Qual o seu sexo[M/F]? ')).upper().strip()

    if idade >= 18:
        contadultos += 1

    if sexo == "M":
        conthomem += 1

    if sexo == "F" and idade < 20:
        contnovinhas += 1

    Continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while Continuar not in "SN":
        Continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()

    if Continuar == "N":
        break

    print('-**-' * 20)
print(f'Há {contadultos} maiores de 18, {conthomem} homens, e {contnovinhas} mulheres menores de 20 anos.')

print("-=" * 40)

totalgasto = contCaros = 0
listapreco = []

while True:
    nome = str(input('Digite o nome do produto que comprou: '))
    preco = input('Digite o preço do produto: R$')
    while preco.isalpha():
        preco = input('Digite o preço do produto: ')
    preco = float(preco)
    listapreco += [preco]

    totalgasto += preco
    if preco > 1000:
        contCaros += 1

    if min(listapreco) >= preco:
        baratao = nome

    Continuar = str(input("Quer continuar?[S/N] ")).upper().strip()
    while Continuar not in "SN":
        Continuar = str(input('Quer continuar?[S/N] ')).upper().strip()

    if Continuar == "N":
        break
print(
    f'o total gasto foi RS {totalgasto:.2f}, {contCaros} produtos custaram mais que R$ 1000.00, e o produto mais barato foi {baratao}')

print("-=" * 40)

cedula1 = cedula10 = cedula20 = cedula50 = 0

while True:
    Valor = input('Digite o valor que deseja sacar: ')
    while not Valor.isnumeric():
        Valor = input('Digite o valor que deseja sacar: ')
    Valor = int(Valor)

    if Valor >= 50:
        cedula50 = int(Valor / 50)
        Valor = Valor - (50 * cedula50)

    if Valor >= 20:
        cedula20 = int(Valor / 20)
        Valor = Valor - (20 * cedula20)

    if Valor >= 10:
        cedula10 = int(Valor / 10)
        Valor = Valor - (10 * cedula10)

    if Valor >= 1:
        cedula1 = int(Valor / 1)
        Valor = Valor - (1 * cedula1)

    if Valor == 0:
        break

print(f'''Vão ser: 
{cedula50} notas de 50
{cedula20} notas de 20 reais
{cedula10} notas de 10 reais
{cedula1} notas de 1 real''')

print("-=" * 40)
