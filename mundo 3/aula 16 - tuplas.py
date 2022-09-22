"""
tuplas são como listas, variáveis com vários objetos dentro:

ex1:
lanche = ('hamburguer', "suco", "pudim", "cereja")
print(lanche[1])
print(lanche[1:3])
print(lanche[-2:])

ex2:
for comida in lanche:
    print(comida)
print('comi pakas')

ex3:
for c in range(0, len(lanche)):
    print(f"com {lanche[c]}")
print("é isso")

ex4:
for a, c in enumerate(lanche):
    print(f"eu vou comer {c} na posição {a}.")

ex5:

a = (2, 5, 4, 1)
b = (2, 3, 3)
c = a + b
print(c)
print(sorted(c))    # sorted usado para ordem alfebética/numérica
print(c.count(2))    # conta a quantidade de "2" dentro da tupla
print(c.index(2, 3))    # o primeiro é identificar a variável e mostrar a posição dela, e o segundo é a partir de qual posição deve indicar

pessoa = ('Marcos', 26, "M", 60.00, True)   # a tupla pode ter multiplos tipos de variável
del pessoa     # o del deleta a variável


"""

e = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez")
x = ("Onze", "Doze", "Treze", "Catorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
extenso = e + x
i = input("Digite um número inteiro de 0 a 20: ")

while True:
    if i.isnumeric():
        i = int(i)
        if i < 0 or i > 20:
            i = (input("Digite novamente, um número inteiro de 0 a 20: "))
        else:
            break
    else:
        i = (input("Digite novamente, um número inteiro de 0 a 20: "))

print(f"você digitou o número {extenso[i]}")

print("*-*-*-"*20)

times = ("Atlético MG", "Palmeiras", "Flamengo", "Bragantino", "Fortaleza",
         "Corinthans", "Internacional", "Fluminence", "Cuiabá", "América MG", "Atlético GO", "São Paulo", "Ceará SC",
         "Atletico PR", "Santos", "Bahia", "Sport Recife", "Juventude", "Grêmio", "Chapecoence")

print(f"Lista de times do Brasilerão: {times}")

print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os ultimos 4 colocados são {times[-4:]}')
print(f'Em ordem alfabética os times ficam: {sorted(times)}')
print(f'O chapecoence está na posição {times.index("Chapecoence")+1}º.')

print("*-*-*-"*20)

from random import randint

a = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os valores sorteados foram: {a[0]} {a[1]} {a[2]} {a[3]} {a[4]} ')
print(f'O maior valor sorteado foi: {max(a)}')
print(f'O menor valor sorteado foi: {min(a)}')

print("*-*-*-"*20)

a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))
d = int(input("Digite um número: "))

abcd = (a, b, c, d)
print(f'Você digitou os valores: {abcd}')


print(f'O valor 9 apareceu {abcd.count(9)} vezes')

if 3 in abcd:
    print(f'O primeiro valor 3 foi digitado na posição {abcd.index(3)+1}.')
else:
    print("Não foi digitado o valor 3 em nenhuma posição")


print(f'Os números pares foram:', end= " ")
for c in range(0, 4):
    if abcd[c] % 2 == 0:
        print(abcd[c], end=" ")

print("")
print("*-*-*-"*20)

listagem = ("Lápis", 1.75, 'Borracha', 2, 'Caderno', 15, 'estojo', 25, "transferidor", 4.2)

print("-"*68)
print(f'{"LISTAGEM DE PREÇOS":^68}')
print("-"*68)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c].title():.<60}R${float(listagem[c+1]):>6.2f}')

print("-"*68)

print("*-*-*-"*20)

palavras = ("lapis", 'caneta', 'homem', 'curso', 'chupa', 'penis', 'mulher', 'futuro', 'passado', 'paralelepipedo')

for c in range(0, len(palavras)):
    print("")
    print(f'Na palavra {palavras[c].upper()} temos ', end="")
    for i in range(0, len(palavras[c])):
        if palavras[c][i].upper() in "AEIOU":
            print(palavras[c][i].lower(), end=" ")


print("")
print("*-*-*-"*20)
