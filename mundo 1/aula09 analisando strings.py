"""
frase = '   curso em video python   '
print(frase[9:21])
print(frase[:21])
print(frase[9::2])
print(frase[::2])
len(frase)
print(frase.count('o', 0, 13))
print(frase.find('deo'))
'curso' in frase
frase.replace('python', 'Android')
print(frase.upper())
frase.lower()
frase.capitalize()
frase.title()
frase.strip()    =  tira os espaos do fim e do inínio da frase
frase.rstrip()   =  tira os espaços pela direita
frase.lstrip()  =   tira os espaços pela esquerda
frase.split()   =   separa os espaços das palavras em frases únicas
'-'.join(frase)  = coloca um "-" entre os espaços
"""

NC = input('Digite seu nome completo: ')
print("Seu nome em maiúsculas é: {}".format(NC.upper()))
print('Seu nome em minúsculas é: {}'.format(NC.lower()))
print('Seu nome tem {} letras.'.format(len(NC.replace(" ", ""))))
ListaNC = NC.split()
print('Seu primeiro nome é {} e contém {} letras.'.format(ListaNC[0], len(ListaNC[0])))

Num = input('Digite um número de 0 a 9999: ')
Num = '{:>4}'.format(Num)
print('''Seu numero contém:'
      Unidade: {}
      Dezena: {}
      Centena: {}
      Milhar: {}'''.format(Num[3], Num[2], Num[1], Num[0]))


Cidade = input('Digite o nome de sua cidade: ').strip()
R1 = Cidade.split()
R2 = str('SANTO' in R1[0].upper())
solucao1 = R2.replace('True', 'Sua cidade começa com a palavra SANTO.')
solucao2 = solucao1.replace('False', 'Sua cidade não começa com a palavra SANTO.')
print(solucao2)

Nome = input('Digite seu nome: ')
Resp = str('SILVA' in Nome.upper())
solucao3 = Resp.replace('True', 'Seu nome contém a palavra SILVA.')
solucao4 = solucao3.replace('False', 'Seu nome não contém a palavra SILVA.')
print(solucao4)

Frase = input('escreva uma Frase: ').strip()
Letras = Frase.lower().count('a')
print('''Sua frase contém {} letras 'a'.'''.format(Letras))
print('A primeira letra a fica na posição {}'.format(int(Frase.lower().find('a'))+1))
print('A última letra a fica na posição {}'.format(int(Frase.lower().rfind('a'))+1))

NomeZ = input('Digite seu nome inteiro: ').strip()
NomeI = NomeZ.split()
print('''Primeiro nome: {}
Último nome: {}'''.format(NomeI[0], NomeI[int(len(NomeI))-1]))
