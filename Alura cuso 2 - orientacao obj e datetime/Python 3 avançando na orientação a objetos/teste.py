"""
class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Temporadas: {vingadores.duracao} - Likes: {vingadores.likes}")

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")
"""

# ex: 1


class Bola:
    def __init__(self, cor, circunferencia, material):
        self._cor = cor
        self.circunf = circunferencia
        self.material = material

    def troca_cor(self, cor_final):
        print(f"a cor foi alterada de {self._cor} para {cor_final}")
        self._cor = cor_final

    def mostra_cor(self):
        print(f'a cor atual é {self._cor}')


bola = Bola("amarela", 45, "eslastico")
bola.mostra_cor()
bola.troca_cor("vermelha")
bola.mostra_cor()

# ex: 02


class Quadrado:
    def __init__(self, lado):
        self._lado = lado

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, novo_lado):
        self._lado = novo_lado

    def Area(self):
        area = self._lado * self._lado
        return area


quadro = Quadrado(2)
print(quadro.lado)
quadro.lado = 3
print(f"O Lado foi alterado para {quadro.lado} com sucesso.")
print(f"A área do quadro é {quadro.Area()}")
quadro.lado = 10
print(f"A área do quadro é {quadro.Area()}")

# ex: 03
import math


class Retangulo:
    def __init__(self, comprimento, largura):
        self._comprimento = comprimento
        self._largura = largura

    @property
    def largura(self):
        return self._largura

    @property
    def comprimento(self):
        return self._comprimento

    def novos_lados(self, novo_comprimento, nova_largura):
        self._comprimento = novo_comprimento
        self._largura = nova_largura

    def area(self):
        area = self._largura * self._comprimento
        return area

    def perimetro(self):
        perimetro = (self._largura * 2) + (self._comprimento * 2)
        return perimetro


def calcula_rodape(largura_do_rodape, perimetro_local):
    n_rodape = math.ceil(perimetro_local / largura_do_rodape)
    return f"A quantidade de rodape será {n_rodape}."


def calcula_piso(area_piso, area_local):
    n_pisos = math.ceil(area_local / area_piso)
    return f"A quantidade de pisos será {n_pisos}."


rodape = Retangulo(15, 10)
rodape.novos_lados(5, 10)
print(rodape.largura)
print(rodape.comprimento)
print(f"A área é {rodape.area()} e o perimetro é {rodape.perimetro()}")

print(calcula_rodape(rodape.largura, 500.01))
print(calcula_piso(rodape.area(), 5000.01))

# ex: 04


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def envelhecer(self, ano):
        for a in range(0, ano):
            if self._idade < 21:
                self._idade += 1
                self._altura += 0.05
            else:
                self._idade += 1

    def engordar(self, peso):
        self._peso += peso

    def emagrecer(self, peso):
        self._peso -= peso

    def crescer(self, altura):
        self._altura += altura

    @property
    def peso(self):
        return self._peso

    @property
    def idade(self):
        return self._idade

    @property
    def altura(self):
        return self._altura


Marcos = Pessoa("Marcos", 15, 75, 1.5)
Marcos.engordar(5)
print(f"Marcos comeu um pudim e engordou 5 kg, ficando com {Marcos.peso} Kgs")
Marcos.envelhecer(5)
print(f"5 anos depois marcos ficou com {Marcos.idade} anos e {Marcos.altura:.2f} metros.")
Marcos.envelhecer(5)
print(f"5 anos depois marcos ficou com {Marcos.idade} anos e {Marcos.altura:.2f} metros.")
Marcos.envelhecer(5)
print(f"5 anos depois marcos ficou com {Marcos.idade} anos e {Marcos.altura:.2f} metros.")


# ex: 05


class conta_corrente:
    def __init__(self, numero, nome, saldo=0):
        self._numero = numero
        self._nome = nome
        self._saldo = saldo

    def alterar_nome(self, novo_nome):
        self._nome = novo_nome

    def saque(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print('saldo insuficiente para o saque.')

    def deposito(self, valor):
        self._saldo +=valor

    def __str__(self):
        return f"saldo atual da conta é {self._saldo}"


conta1 = conta_corrente("01", "Marcos")
print(conta1)
conta1.deposito(5000)
print(conta1)
conta1.saque(1000)
print(conta1)
conta1.saque(60000)
print(conta1)

# ex: 06


class TV:
    def __init__(self, TV=False):
        self.TV = TV
        if TV:
            self.TV = False
        else:
            self.TV = True
        self._volume = 50
        self._canal = 5
        self._lista_canal = [1, 2, 3, 4, 5]

        self._lista_volume = []
        for volume in range(0, 101):
            self._lista_volume += [volume]

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, valor):
        if valor in self._lista_volume:
            self._volume = valor
        else:
            print("EERO ESTE VOLUME NÃO EXISTE")

    @property
    def canal(self):
        return self._canal

    @canal.setter
    def canal(self, canal):
        if canal in self._lista_canal:
            self._canal = canal
        else:
            print("ERRO, este canal não existe")


tv = TV()
print(tv.volume)
