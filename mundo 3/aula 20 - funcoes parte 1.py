"""
def mostralinha(txt):
    print('-------------------')
    print(txt)
    print("-------------------")


mostralinha("olá")


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


soma(b=4, a=5)
soma(8, 9)
soma(2, 1)

contador(1, 2, 5)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
"""

print("-" * 30)
print('Exercicio 1')


def área(lar, f):
    a = lar * f
    print(f'A área do terreno de {lar}x{f} é {a} m².')


Largura = float(input('LARGURA (M): '))
Comprimento = float(input('COMPRIMENTO (M): '))

área(Largura, Comprimento)

print("-" * 30)
print('Exercicio 2')


def escreva(a):
    b = int(len(a))
    print("~" * (b + 2))
    print(f' {a}')
    print("~" * (b + 2))


c = str(input("Escreva algo: ")).strip()
escreva(c)

print("-" * 30)
print('Exercicio 3')


def contador(i, f, p):
    lista = []
    for c in range(i, f+1, p):
        lista += [c]
    for c in range(i, f-1, -p):
        lista += [c]
    print(lista)


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input('INICIO: '))
fim = int(input('FIM: '))
pas = int(input('Passo: '))
if pas < 0:
    pas = pas*(-1)
elif pas == 0:
    pas = 1
contador(ini, fim, pas)


print("-" * 30)
print('Exercicio 4')


def maior(* n):
    tam = len(n)
    print("-="*30)
    for c in range(tam):
        print(n[c], end=" ")
    print(f'Foram informados {tam} valores ao todo.')
    if n == ():
        print(f'O maior valor foi {0}.')
    else:
        print(f'O maior valor foi {max(n)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

print("-" * 30)
print('Exercicio 5')
from random import randint


def sorteio(lista):
    for c in range(0, 5):
        a = randint(0, 10)
        lista.append(a)


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lista}, temos {soma}.')


num = []
sorteio(num)
print(num)
somapar(num)
