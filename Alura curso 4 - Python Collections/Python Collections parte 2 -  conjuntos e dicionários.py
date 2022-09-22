class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self. saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>> Codigo {self.codigo} Saldo {self.saldo} <<]"


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)


conta_do_gui = ContaCorrente(15)
print(conta_do_gui)

conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(13544)
conta_da_dani.deposita(324)
print(conta_da_dani)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
    print(conta)

banco = {"agencia": 77, "contas": contas}
print(banco)

deposita_para_todas(banco["contas"])
for conta in contas:
    print(conta)

