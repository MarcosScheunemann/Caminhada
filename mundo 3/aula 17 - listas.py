"""
Listas:
lista = [1, 2, 3]
ou
lista = list(1, 2, 3)

lista1 = lista 2       => você acaba gerando um link entre as duas lista, e um será igual a outra.
lista1 = lista2[:]     => faz a lista 1 uma cópia da lista 2 no estado em que estiver no momento.
lista[1] = 10        => faz o indice 1 (que é o 2) virar um 10.
lista.append(7)         => adiciona um número à lista.


lista.pop()           => retira o ultimo valor da lista
lista.pop(indice)           => retira o valor do indice na lista
lista.remove('1')     => retira um elemento indicado da lista, se houver multiplos iguais, ele remove o indice mais baixo
lista.sort()          => deixa em ordem a lista, crescente ou alfabética
lista.sort(reverse = True)          => deixa em ordem a lista, decrescente ou anti-alfatébica
len(lista)                          => diz o número de elementos dentro da lista.

ex de criação de lista:

for c, v in enumerate(lista):
    print(f'Na posição {c} encontrei o valor {v}.')
print('cheguei no final da lista')

lista2 = []
for c in range(0, 5):
    lista2 += [int(input('Digite um valor: '))]
print(lista2)
"""

print('exercício 1:')

lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a lista para a posição {c}: ')))

print(f'Você digitou os valores {lista}')

maiores = []
menores = []
for c, v in enumerate(lista):
    if v == max(lista):
        maiores.append(c)
    elif v == min(lista):
        menores.append(c)
print(f'O maior valor digitado foi o {max(lista)} nas posições:', end=" ")
for c in range(len(maiores)):
    print(maiores[c], end="... ")
print("")
print(f'O menor valor digitado foi o {min(lista)} nas posições: ', end="")
for c in range(len(menores)):
    print(menores[c], end="... ")
print("")

print('+=='*20)

print('exercício 2:')

lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = " "
    while continuar not in "SsNn":
        continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == "N":
        break

lista.sort()
print(f'Você digitou os valores {lista}')

print('+=='*20)

print('Execicio 3: ')

lista = []
for c in range(0, 5):
    valor = int(input('Digite um Valor: '))
    if len(lista) == 0:
        lista.append(valor)
        print(f'Adicionado à lista...')
    elif valor > max(lista):
        lista.append(valor)
        print(f'Adicionado ao final da lista...')
    elif valor < min(lista):
        lista.insert(0, valor)
        print(f'A dicionado na posição 0 da lista...')
    else:
        for b, v in enumerate(lista):
            if lista[b] < valor < lista[b + 1]:
                lista.insert(b + 1, valor)
                print(f'Adicionado na posição {b + 1} da lista...')
                break

print(f'Os valores digitados em ordem foram {lista}')

print('+=='*20)

print('Execicio 4: ')

lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input("Quer continuar? [S/N]")).upper()
    while continuar not in "SsNn":
        continuar = str(input('Quer continuar? [S/N?')).upper()
    if continuar == "N":
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista.')

print('+==' * 20)

print('Execicio 5: ')

lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    continuar = str(input("Quer continuar? [S/N]")).upper()
    while continuar not in "SsNn":
        continuar = str(input('Quer continuar? [S/N?')).upper()
    if continuar == "N":
        break

print(f'A lista completa é {lista}')

listap = []
listai = []

for c in range(len(lista)):
    valor = lista[c]
    if valor % 2 == 0:
        listap.append(valor)
    else:
        listai.append(valor)
print(f'A lista de pares é {listap}')
print(f'A lista de ímpares é {listai}')

print('+==' * 20)

print('Execicio 6: ')

ex = str(input("Digite uma expressão para ver se é válida:   ")).split()
lista = []

for c in range(len(ex)):
    for d in range(len(ex[c])):
        lista.append(ex[c][d])

cont = 0
listaparentese = []

while True:
    if lista[cont] == "(":
        listaparentese.append(lista[cont])
    elif lista[cont] == ")":
        listaparentese.append(lista[cont])
    cont += 1
    if cont >= len(lista):
        break

cont2 = 0
pont = 0
while True:
    if listaparentese[cont2] == "(":
        pont += 1
    elif listaparentese[cont2] == ")":
        pont -= 1

    if pont < 0:
        print('esta expessão é inválida! ')
        break
    cont2 += 1
    if cont2 == len(listaparentese):
        if pont == 0:
            print('Esta expessão é válida! ')
        else:
            print('Esta expressão é inválida! ')
        break

