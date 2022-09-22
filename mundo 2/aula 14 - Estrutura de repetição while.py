"""
Aula 14 – Estrutura de repetição while:

ex 1 :
c = 1
while c != 10:
    print(c)
    c += 1
print('Acabou')

ex 2 :

n = "a"
par = impar = 0
while n != 0:
    if n != 0:
        n = int(input("Digite um valor: "))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("você digitou {} números pares e {} números ímpares.". format(par, impar))

"""

sexo = str(input('Informe seu sexo: [F/M]:  ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('sexo incorreto, favor digite seu sexo: ')).strip().upper()
print('muito bem.')

print('--=--'*20)

from random import randint

Num = int(randint(1, 10))
palpites = 0
chute = 0
while Num != chute:
    chute = int(input('Digite um valor de 1 a 10: '))
    if Num != chute:
        print('Que pena, ERROU!')
        palpites += 1
print('muito bem! acertou! só precisou de {} palpites.'.format(palpites + 1))

print('--=--'*20)

valor1 = "a"
valor2 = "b"
opcao = 0
while opcao != 5:
    valor1 = float(input('Digite o primeito valor: '))
    valor2 = float(input('digite o segundo valor: '))
    opcao = int(input('''
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos números
    [5] - sair do programa
    :  '''))
    if opcao == 1:
        print('A soma dos valores é {:.2f}.'.format(valor1 + valor2))
    elif opcao == 2:
        print('A multiplicação dos dois números é {:.2f}.'.format(valor1 * valor2))
    elif opcao == 3:
        print('O maior número é {}.'.format(max(valor1, valor2)))
    elif opcao == 4:
        print('Tudo bem, vamos com outros números!')
    elif opcao == 5:
        opcao = 5
    else:
        print('opção incorreta, tente novamente.')

print('Tudo bem, Adeus.')

print('--=--'*20)

fat = 1
Num = int(input('Digite um número para saber seu fatorial: '))
resultado = 1

while fat != (Num + 1):
    resultado *= fat
    fat += 1
print(resultado)

# OU

total = 1
Num = int(input('digite um número para saber seu fatorial: '))

for c in range(1, Num+1):
    total *= c
print(total)

print('--=--'*20)

inicio = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
r = 1
fim = inicio + razao * 10
while inicio != fim:
    print(inicio, end=' => ')
    inicio += razao
print("CABO")

print('--=--'*20)

inicio = int(input('Digite o primeiro termo de uma PA: '))
razao = int(input('Digite a razão da PA: '))
r = 1
fim = inicio + razao * 10
while inicio != fim:
    print(inicio, end=' => ')
    inicio += razao
print('Por enquanto é isso.')

a = int(input('E agora? deseja ver mais quantos termos? '))
final = fim + razao * a
while a != 0:
    if fim >= final:
        a = int(input("E agora? deseja ver mais quantos termos?? "))
        final = fim + razao * a
    while fim < final:
        print(fim, end=" => ")
        fim += razao
print('tudo bem, chega.')

print('--=--'*20)

n = int(input('digite quantos termos deseja ver de uma sequência de Fibonacci: '))
i = 0
listaF = []
index = 0
while index <= n-1:
    if i == 0:
        listaF += [i]
        index += 1
        print(i, end=", ")
        i += 1
    elif i == 1:
        print(i, end=", ")
        listaF += [i]
        index += 1
        i = (listaF[index - 2] + listaF[index - 1])
    else:
        i = (listaF[index - 2] + listaF[index - 1])
        print(i, end=", ")
        listaF += [i]
        index += 1
print('CABO')

print('--=--'*20)

listValores = []
index = 0
Num = 0
while Num != 999:
    valor = int(input('Digite um valor: '))
    if valor == 999:
        Num = 999
    else:
        listValores += [valor]
        index += 1
print('A soma de todos os valores digitados é {} e você digitou {} números'.format(sum(listValores), index))

print('--=--'*20)

from statistics import mean

continuar = ""
listValores = []
while continuar != 'N':
    valor = int(input('Digite um valor: '))
    listValores += [valor]
    continuar = str(input('Quer continuar? (S/N): ').upper())
print('a média dos valores que colocou é {:.2f}, o menor é {}, e o maior é {}.'.format(mean(listValores), min(listValores), max(listValores)))

print('--=--'*20)
