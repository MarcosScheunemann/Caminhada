import re # Regular expression

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # obj Match

if busca:
    cep = busca.group()

"""
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambio

"""
site = "https://www.bytebank.com.br/cambio"


padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)/cambio")
url = padrao_url.match(site)

if url:
    sitezao = url.group()
    print(sitezao)
