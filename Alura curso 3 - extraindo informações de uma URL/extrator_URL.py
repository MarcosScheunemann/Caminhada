import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia.")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self.url.find("?")
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        if self.get_url_parametro().find(parametro_busca) == -1:
            raise ValueError("Parâmetro inválido")
        else:
            indice_parametro = self.get_url_parametro().find(parametro_busca)
            indice_valor = indice_parametro + len(parametro_busca) + 1
            indice_e_comercial = self.get_url_parametro().find("&", indice_valor)

            if indice_e_comercial == -1:
                valor = self.get_url_parametro()[indice_valor:]
            else:
                valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
            return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametro() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        if self.url == other.url:
            return True
        else:
            return False


def conversor(moeda_origem, moeda_destino, quantidade):
    if moeda_origem == "dolar" and moeda_destino == "real":
        valor = float(quantidade) * VALOR_DOLAR
        print(valor)
    elif moeda_origem == "real" and moeda_destino == "dolar":
        valor = float(quantidade) / VALOR_DOLAR
        print(valor)
    else:
        raise ValueError("Moeda indisponível para conversão")
"""
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)

print(len(extrator_url))
print(extrator_url)

sera = extrator_url == extrator_url2
print(sera)
"""

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

conversor(moeda_origem, moeda_destino, quantidade)
