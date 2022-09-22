"""
Aula 13 - estrutura de repetição:
exemplo 1:
for c in range(0, 4):
    print(c)
print('Acabou')

range (a, b, c)
a = início
b = fim
c = método, ex: se for 2, ele vai de dois em dois, se for -1, ele contra para trás

a, b, c podem ser alterados em variáveis.
ex 2:
n = int(input("digite até quanto quer contar: ")
for c in range(0, n+1):
    print(c)
print('Acabou')

ex 3: somatória

soma = o
for c in range(0, 4):
    n = int(input("digite um número: ")
    soma += n                                               =>   += significa acrescenta ao valor
print('o valor total de sua soma é {}.'.format(soma))


"""
from time import sleep

print('ATENÇÃO QUE LÁ VEM OS FOGOS !!!')
for c in range(10, -1, -1):
    sleep(0.4)
    print(c)
sleep(0.4)
print('CABUUUUUUMMM !!!')

print('--==--'*20)

print('Agora os números pares de 1 a 50:')
for c in range(0, 51):
    if c % 2 == 0 and c > 0:
        print(c, end=" ")
print('são esses os pares.')

print('--==--'*20)

print('Agora a soma dos números impares multiplos de 3 entre 1 e 500:')
s = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            s += c
print("A soma é {}".format(s))

print('--==--'*20)

Num = int(input("Escolha um número de 1 a 10, para ver sua tabuada: "))
for c in range(1, 11):
    print('{} x {} = {}'.format(Num, c, (Num * c)))

print('--==--'*20)

soma = 0
for c in range(1, 7):
    Num = int(input('Digite um número: '))
    if Num % 2 == 0:
        soma += Num
print('A soma de todos os números pares é {}.'.format(soma))

print('--==--'*20)

a = int(input('Digite o primeiro termo do início: '))
r = int(input('Digite a razão para progressão: '))

v = a + r * 10

for c in range(a, v, r):
    print(c, end=" => ")
print("CABO")

print('--==--'*20)

Num = int(input('Digite um número para saber se é um número primo: '))
soma = 0
for c in range(1, Num + 2):
    if Num % c == 0:
        soma += Num
if soma == 2 * Num:
    print("É um número primo.")
else:
    print('Não é um número primo')

print('--==--'*20)

frase = str(input('Digite uma frase para ser se é um palíndramo: ')).strip().upper()
frase = frase.replace(" ", "")
vazio = str("")
for c in range(len(frase)-1, -1, -1):
    vazio += frase[c]
if vazio == frase:
    print('É um palíndromo.')
else:
    print('não é um palíndromo.')

print('--==--'*20)

print('Contador de pessoas de Maior, insira abaixo os anos de nascimento:')
# maior idade só com 21 anos.
from datetime import date
anoatual = date.today().year
M = 0
NM = 0
for c in range(1, 8):
    anonasc = int(input('Digite seu ano de nascimento: '))
    if anoatual - anonasc >= 21:
        M += 1
    else:
        NM += 1
print('O número de pessoas maiores é {} e de menores é {}.'.format(M, NM))

print('--==--'*20)

print('Vamos ver qual o Maior e menor peso entre vocês: ')
lista = []
for c in range(1, 6):
    peso = [float(input('Qual o peso da {}ª pessoa?  '.format(c)))]
    lista += peso
print('O maior peso é {:.2f} Kg, e o menor peso é {:.2f} Kg.'.format(max(lista), min(lista)))

print('--==--'*20)

from statistics import mean

print('Vamos ver o nome, idade e sexo agora: ')
listanome = []
listaidade = []
listasexo = []


for c in range(1, 5):
    nome = [str(input('Digite o nome: '))]
    idade = [int(input('Digite a idade: '))]
    sexo = [str(input('Digite o sexo (F para feminino, e M para masculino): ')).upper().strip()]
    listanome += nome
    listaidade += idade
    listasexo += sexo

mediaidade = mean(listaidade)
novinhas = 0
for i in range(0, 4):
    if listasexo[i] == "F":
        if listaidade[i] < 20:
            novinhas += 1
listaIhomem = []
listaNhomem = []

for homem in range(0, 4):
    if listasexo[homem] == "M":
        listaNhomem += [listanome[homem]]
        listaIhomem += [listaidade[homem]]
Ivelho = max(listaIhomem)
velho = ""

for V in range(0, len(listaIhomem)):
    if Ivelho == listaIhomem[V]:
        velho += listaNhomem[V]

print('A média de idade é {}'.format(mediaidade))
print('O homem de maior idade é {}'.format(velho))
print('No grupo contém {} mulheres menores de 20 anos.'.format(novinhas))

print('--==--'*20)