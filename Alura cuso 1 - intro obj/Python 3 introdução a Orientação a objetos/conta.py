class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def extrato(self):
        print(f"o titular é {self.__titular}, e o saldo é {self.__saldo:.2f}.")

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        return self.__saldo + self.__limite >= valor

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f"ERRO !! sem saldo o suficiente para sacar {valor:.2f} reais!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"


# Pode utilizar o "from conta import Conta" para importar uma classe.

numero_da_conta = 1
n1 = input(str("Qual o titular? ")).title()
n2 = input(str("Qual o titular? ")).title()
saldo = 0
limite = 5

titular1 = Conta(numero_da_conta, n1, saldo, limite)
titular2 = Conta(numero_da_conta, n2, saldo, limite)

titular1.extrato()

titular1.deposita(50)

titular1.extrato()

titular1.transfere(60, titular2)

titular1.extrato()
titular2.extrato()


print(titular1.limite)

titular1.limite = 3000

print(titular1.limite)



