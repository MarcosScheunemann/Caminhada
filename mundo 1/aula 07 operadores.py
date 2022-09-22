# Operadores:
# adição +
# subtração -
# multiplicação *
# divisão /
# potência **
# Divisão Inteira //
# Resto da divisão %
# igual ==

#print("{:20}".format(n1)) = mostra em 20 espaços
#print("{:>20}".format(n1)) = mostra à direita
# print("{:<20}".format(n1)) = mostra à esquerda
# print("{:^20}".format(n1)) = mostra centralizado
# print("{:=^20}".format(n1)) = centraliza e coloca "="para preencher
# print("{:.3f}".format(n1)) =  tres casas decimais, tipo, flutuante (ex: 2.363636)

#  \n  = quebra a linha
#  end= ""   = continua a linha

n1 = int(input("Digite um número inteiro:"))
print("seu antecessor é {} e seu Sucessor é {}".format(n1-1, n1+1))
print("e também seu dobro é {}, o triplo é {} e sua raiz quadrada é {:.2f}".format(n1*2, n1*3, n1**(1/2)))

nota1 = int(input("digite sua nota do primeiro bimestre"))
nota2 = int(input("digite sua nota do segundo bimestre"))
print("Sua média final é {:.2f}".format((nota1+nota2)/2))

metros = int(input("Digite o valor em metros para ser convertido: "))
print("São {}KM".format(metros/1000))
print("São {}Hm".format(metros/100))
print("São {}Dam".format(metros/10))
print("São {}Dm".format(metros*10))
print("são {}Cm".format(metros*100))
print("são {}Mm".format(metros*1000))

V = int(input("Digite o valor que deseja ver sua tabuada: "))
print("{} x 1 = {:2}".format(V, V*1))
print("{} x 2 = {:2}".format(V, V*2))
print("{} x 3 = {:2}".format(V, V*3))
print("{} x 4 = {:2}".format(V, V*4))
print("{} x 5 = {:2}".format(V, V*5))
print("{} x 6 = {:2}".format(V, V*6))
print("{} x 7 = {:2}".format(V, V*7))
print("{} x 8 = {:2}".format(V, V*8))
print("{} x 9 = {:2}".format(V, V*9))
print("{} x 10 = {:2}".format(V, V*10))

M = float(input("Digite quantos reais você tem: R$ "))
print("Você pode comprar US${:.2f}".format(M/5.67))

L = float(input("Digite a largura de sua parede em metros:"))
H = float(input("digite a altura da parede em metros:"))
A = L * H
print("a área de sua parede é {:.2f}m², e vai precisar de {:.2f} litros de tinta".format(A, A/2))

P = float(input("digite o preço de seu produto: "))
print("com 5% de desconto seu produto fica em um valor de {:.2f} reais".format(P*0.95))

S = float(input("Digite seu salário: "))
print("Com o aumento de 15%, seu salário fica em {:.2f} reais".format(S*1.15))

C = float(input("Digite a tempratura em °C:"))
print("São {}°F".format((C*9)/5+32))

Km = int(input("Quantos foram os Kilometros rodados? "))
D = int(input("Quantos dias o carro foi alugado? "))
P = (D*60)+(0.15*Km)
print("o Preço a pagar pelo aluguel é R${:.2f}".format(P))

