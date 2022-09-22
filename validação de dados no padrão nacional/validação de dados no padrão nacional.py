from validate_docbr import CPF, CNPJ
import re
from datetime import datetime, timedelta
from time import sleep


class Doc:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento.strip().lower()
        documento = str(documento)
        if self.tipo_documento == "cpf":
            self.cpf = self.cpf_eh_valido(documento)
        elif self.tipo_documento == "cnpj":
            self.cnpj = self.cnpj_eh_valido(documento)
        else:
            raise ValueError("Documento selecionado inválido, deve escolher cpf, ou cnpj")

    def cpf_eh_valido(self, documento):
        validador = CPF()
        if validador.validate(documento):  # aqui chamamos uma função da importação do CPF validate()
            return documento
        else:
            raise ValueError("CPF inválido!")

    def formatacao(self):
        if self.tipo_documento == "cpf":
            mascara = CPF()
            return mascara.mask(self.cpf)  # aqui chamamos outra função do CPF mask()
        elif self.tipo_documento == "cnpj":
            mascara = CNPJ()
            return mascara.mask(self.cnpj)  # aqui chamamos outra função do CNPJ mask()

    def cnpj_eh_valido(self, documento):
        validador = CNPJ()
        if validador.validate(documento):
            return documento
        else:
            raise ValueError("CNPJ inválido")  # aqui chamamos uma função da importação do CNPJ validate()

    def __str__(self):
        return self.formatacao()


class TelefonesBr:
    def __init__(self, telefone):
        self.telefone = telefone
        if self.valida_telefone():
            self.numero = telefone
        else:
            raise ValueError("Numero incorreto")

    def valida_telefone(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, self.telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        if len(self.numero) == 13:
            padrao = "([0-9]{2})?([0-9]{2})(\d+)([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao, self.numero)
            numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}{resposta.group(4)}-{resposta.group(5)}"
        else:
            padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
            resposta = re.search(padrao, self.numero)
            numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado

    def __str__(self):
        return self.format_numero()


class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        self.hoje_formatada = self.momento_cadastro.strftime("%d/%m/%Y , às %H:%M")

    def mes_cadastro(self):
        meses_do_ano = ("", "janeiro", "fevereiro", "março", "abril", "maio", "junho",
                        "julho", "agosto", "setembro", "outubro", "novembro", "dezembo")
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        semana = ("segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo")
        dia_semana = self.momento_cadastro.weekday()
        return semana[dia_semana]

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=30) - self.momento_cadastro
        return tempo_cadastro

    def __str__(self):
        return f"Foi feito o cadastro em {self.hoje_formatada}."


# programa principal

cpf = Doc(43077527839, "CPF")
cnpj = Doc(42591651000143, "cnpj")

print(cnpj)
print(cpf)

texto_com_telefone = "ahbqagwevf qwefhbieb oc  qwqe rwe65146w ef  cf 561 5511982003157 ahsbdiabsd"
telefone_obj = TelefonesBr(texto_com_telefone)

print(telefone_obj)

cadastro = DatasBr()

print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)
print(cadastro.tempo_cadastro())
