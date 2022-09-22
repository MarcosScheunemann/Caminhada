# utilizar módulos para importar funcionalidades a partir do math


from math import floor, hypot, sin, tan, cos, radians
from random import choice, shuffle



# math.ceil = arredonda para cima em número inteiro
# utilizar o from math import **** = faz com o que não precisa escrever o math antes.
# em https://docs.python.org/3.10/library - consegue encontrar uma biblioteca para uso
# de fórmulas e módulos adicionais diversos.


num = float(input('Digite um número: '))
n2 = floor(num)
print('o número inteiro de {} é {}'.format(num, n2))

v1 = float(input('comprimento do cateto oposto: '))
v2 = float(input('comprimento do cateto adjacente: '))
v3 = hypot(v1, v2)
print('o comprimento da hipotenusa é: {:.2f}'.format(v3))

a1 = float(input('digite o ângulo em graus: '))
print('seu seno é {:.2f}, seu cos é {:.2f}, e sua tangente é {:.2f}.'.format(sin(radians(a1)), cos(radians(a1)), tan(radians(a1))))

Alunos = [input('Digite o primeiro aluno: '), input('o segundo: '), input('o terceiro:'), input('o quarto: ')]
AlunoEscolhido = choice(Alunos)
shuffle(Alunos)
print('O aluno escolhido para limpar a lousa é {}.'.format(AlunoEscolhido))
print('E sua sequência de apresentação é {}, {}, {} e por ultimo {}.'.format(Alunos[0], Alunos[1], Alunos[2], Alunos[3]))
