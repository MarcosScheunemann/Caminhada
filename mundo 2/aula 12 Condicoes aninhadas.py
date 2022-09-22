"""
condicionais aninhadas:
exemplo1:
x = ('digite um número')
if x == 3:
    print('bloco 1')
elif x == 4:                                => mais de duas condições usa-se o elif
    print('bloco 2')
else:                                     => só utilizado para executar caso nenhuma seja verdadeira, não é pbrigatório
    print('bloco 4')
print('FIM')

Exemplo 2 :
nome = str(input('Qual é o seu nome??'))
if nome == 'Gustavo':
    print('seu nome é bonito!')
elif nome =='Predro' or nome =='Maria':
    print('nome popular')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('nome de gata')
else:
    print('seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))

"""

vcasa = float(input('Qual o valor da casa? '))
Sal = float(input('Qual o seu salário? '))
tempo = float(input('Quantos anos deseja pagar a casa? '))
lucro = vcasa * 0.20
CPrest = ((vcasa/tempo) / 12) + (lucro / (tempo * 12))
if Sal * 0.30 > CPrest:
    print('Foi aprovado o empréstimo bancário em parcelas de {:.2f} reais por mês, em {} meses.'.format(CPrest, int(tempo * 12)))
else:
    print('desculpe, vccê é muito pobre para esse empréstimo.')
print('Tenha um bom dia!')

print('--=--' * 20)

Num = int(input('Escreva um número inteiro para converção: '))
BC = int(input("""Digite:
               1 para binário.
               2 para octal.
               3 para hexagonal.
                
                :  """))
if BC == 1:
    FIM = bin(Num)[2:]
elif BC == 2:
    FIM = oct(Num)[2:]
elif BC == 3:
    FIM = hex(Num)[2:]
else:
    FIM = str('NADA')
    print("Voce optou por escolher nenhuma opção, que pena.")
print("Seu número na conversão escolhida é {}.".format(FIM))

print('--=--' * 20)

v1 = int(input('Escreva o primeiro valor inteiro: '))
v2 = int(input('Escreva outro valor inteiro: '))
if v1 == v2:
    print('Não existe valor maior, os dois são iguais.')
elif v1 > v2:
    print('O valor {} é maior que o valor {}.'.format(v1, v2))
elif v2 > v1:
    print('O valor {} é maior que o valor {}.'. format(v2, v1))
else:
    print("você não digitou os valores corretamente")

print('--=--' * 20)

idade = int(input('Qual o ano de seu nascimento? '))
from datetime import date
anoatual = date.today().year
Dif = anoatual - idade
if Dif == 18:
    print('você deve se alistar neste ano!')
elif Dif > 18:
    print('Já passou o tempo de alistamento em {} anos.'.format(Dif - 18))
elif Dif < 18:
    print('Ainda falta {} para você poder se alistar.'.format(18 - Dif))
else:
    print('Algo deu errado!')

print('--=--' * 20)

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2)/2
if m < 5:
    resultado = str('reprovado, média {}'.format(m))
elif 5 <= m <= 6.9:
    resultado = str('recuperação, média {}'.format(m))
elif m > 7:
    resultado = str('APROVADO, média {}.'.format(m))
else:
    resultado = str('Algo deu errado')
print(resultado)

print('--=--' * 20)

ano = int(input('Digite o ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    cat = "MIRIM"
elif 9 < idade <= 14:
    cat = "INFANTIL"
elif 14 < idade <= 19:
    cat = "JUNIOR"
elif 19 < idade <= 20:
    cat = 'SÊNIOR'
else:
    cat = "MASTER"
print('sua categoria é {}.'.format(cat))

print('--=--' * 20)

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 == r2 == r3:
    tipo = 'Equilátero'
elif r1 == r2 or r1 == r3 or r2 == r3:
    tipo = 'Isóceles'
else:
    tipo = 'Escaleno'

if (r2 - r3) < r1 < (r2 + r3) and (r1 - r3) < r2 < (r1 + r3) and (r1 - r2) < r3 < (r1 + r2):
    print('Podem formar um triângulo, e é {}.'.format(tipo))
else:
    print('Essas três retas não podem formar um triangulo.')

print('--=--' * 20)

print('Vamos agora calcular o seu IMC.')
peso = float(input("qual o seu Peso? (em Kg) "))
altura = float(input("qual a sua altura? (em M)"))
IMC = peso / (altura * altura)

if IMC < 18.5:
    status = "Abaixo do peso"
elif 18.5 <= IMC < 25:
    status = "Peso ideal"
elif 25 <= IMC < 30:
    status = "Sobrepeso"
elif 30 <= IMC < 40:
    status = "Obesidade"
else:
    status = "Obesidade mórbita"
print("Seu satatus de IMC é {}".format(status))

print('--=--' * 20)

PN = float(input("Digite o preço de seu produto: "))
CD = int(input("""digite para sua condição de pagamento:
1 - Á vista no dinheiro/cheque.
2 - Á vista no cartão.
3- em até 2x no cartão.
4- 3x ou mais no cartão.
"""))
if CD == 1:
    valorF = PN * 0.90
elif CD == 2:
    valorF = PN * 0.95
elif CD == 3:
    valorF = PN
elif CD == 4:
    valorF = PN * 1.2
else:
    print("número errado digitado.")
    valorF = "erro"
print("seu produto custará no final => {:.2f} reais".format(valorF))

print('--=--' * 20)

print("Agora vamos jogar Jokenpô !!")
from random import choice
NPC = choice(["pedra", "papel", "tesoura"])
Jogada = int(input(""" Digite entre 1 e 3 para jogar:
1- pedra
2- papel
3- tesoura
:  """))
if Jogada == 1:
    Jogadap = "pedra"
elif Jogada == 2:
    Jogadap = "papel"
elif Jogada == 3:
    Jogadap = "tesoura"
else:
    Jogadap = NPC
    print("escolha errada.")
if NPC == Jogadap:
    print("EMPATE!!")
elif NPC == "pedra" and Jogadap == "papel":
    print("VOCÊ GANHOU DA PEDRA!!")
elif NPC == "pedra" and Jogadap == "tesoura":
    print("VOCÊ PERDEU DA PEDRA!!")
elif NPC == "papel" and Jogadap == "tesoura":
    print("VOCÊ GANHOU DO PAPEL!!")
elif NPC == "papel" and Jogadap == "pedra":
    print("VOCÊ PERDEU DO PAPEL!!")
elif NPC == "tesoura" and Jogadap == "papel":
    print("VOCÊ PERDEU PARA TESOURA!!")
elif NPC == "tesoura" and Jogadap == "pedra":
    print("VOCÊ GANHOU DA TESOURA!!")

print('--=--' * 20)
