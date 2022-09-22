import requests


class BuscaEndereco:
    def __init__(self, cep):
        self.cep = str(cep)
        if not self.cep_e_valido():
            raise ValueError("CEP inválido")

    def cep_e_valido(self):
        return len(self.cep) == 8

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def __str__(self):
        return self.format_cep()

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        r = requests.get(url)
        dados = r.json()
        show = f'{dados["logradouro"]}, {dados["bairro"]} - {dados["localidade"]}, {dados["uf"]}'
        return show

# programa principal


cep = "04140110"
obj_cep = BuscaEndereco(cep)
print(obj_cep)

print(obj_cep.acessa_via_cep())
