
#Exemplos de tratamento de erros:

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos problema com os tipos de dados que você digitou')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre"')

import urllib
import urllib.request

print('-=' * 40)
print('Exercicio 1')


def leiaint(num):
    while True:
        algo = input(num)
        try:
            int(algo)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')  # colocando na cor vermelho.
        else:
            return algo


def leiafloat(num):
    while True:
        algo = input(num)
        try:
            float(algo)
        except (ValueError, TypeError, KeyboardInterrupt):
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')  # colocando na cor vermelho.
        else:
            return f'{float(algo):.2f}'


n = leiaint('Digite um número inteiro: ')
q = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n} e o valor reaal foi {q}.')

print('-=' * 40)
print('Exercicio 2')

try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print(f'\033[0;31mERRO! não foi possivel abrir o site.\033[m')  # colocando na cor vermelho.
else:
    print('Muito bem! conseguimos abrir o site.')
