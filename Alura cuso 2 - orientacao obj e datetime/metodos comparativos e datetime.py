"""
https://www.alura.com.br/artigos/como-comparar-objetos-no-python


__eq__(), chamado pelo operador ==
__ne__(), chamado pelo operador !=
__gt__(), chamado pelo operador >
__lt__(), chamado pelo operador <
__ge__(), chamado pelo operador >=
__le__(), chamado pelo operador <=

No nosso caso, como estamos tratando de comparações de igualdade, focaremos no método __eq__() (mas é importante notar a possibilidade de implementação de todos os tipos básicos de comparação!).

Precisamos, primeiro, saber o que queremos que seja comparado. Como precisamos que a comparação foque em algo único de cada filme, usaremos o próprio título. Então vamos implementar:


class Filme():
    ## código omitido
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo
Agora que aplicamos isso ao nosso código, vamos tentar procurar um filme em nosso acervo novamente:


def tenho_o_filme(filme_procurado):
    meus_filmes = pega_todos_os_filmes()
    for filme in meus_filmes:
        if filme_procurado == filme:
            return True
    return False

filme_procurado = Filme(‘A Teoria de Tudo’, ‘James Marsh’)

if tenho_o_filme(filme_procurado):
    print(‘Tenho o filme!’)
else:
    print(‘Não tenho :(‘)
Dessa vez:


console: Tenho o filme!
Certo!


"""
"""
https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python


Para evitar maiores complicações, a classe date soluciona isso com um único método - o strftime(), que toma como parâmetro a formatação que queremos em nossa string de data e, desse modo, nos dá maior liberdade para decidirmos como queremos exibir a data.

Esta formatação usa códigos melhor explicados na documentação. Ao final do texto, também damos uma explicação breve neles. No nosso caso fica assim:

data_em_texto = data_atual.strftime(‘%d/%m/%Y’)
print(data_em_texto)
E agora sim:

01/03/2018
Ou, no caso do nosso exemplo que resultou em 010/010/2018:

10/10/2018
Agora só precisamos dar um jeito de armazenar o horário também. Quem será que pode cuidar disso? Como você deve ter imaginado, o mesmo módulo datetime do qual importamos a classe date também possui classes que facilitam a manipulação de horários.


////


nquanto podemos sim usar o tipo time, destinado exclusivamente para horários, o módulo nos dá uma solução muito mais apropriada para o nosso problema com o tipo datetime - sim, tem o mesmo nome do módulo, cuidado com a confusão!

Uma das vantagens da classe datetime é que ela consegue cuidar da data e do horário ao mesmo tempo. A única diferença em nosso uso é que, em vez do método today(), usaremos o método now():

from datetime import datetime

data_e_hora_atuais = datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime(‘%d/%m/%Y’)

print(data_e_hora_em_texto)
O resultado é como o anterior:

01/03/2018
Opa! Apesar de já estarmos usando a classe datetime, que incorpora o horário, precisamos declarar na formatação que passamos como parâmetro para o strftime() que queremos mostrar a hora e o minuto, também:

data_e_hora_em_texto = data_e_hora_atuais.strftime(‘%d/%m/%Y %H:%M’)

print(data_e_hora_em_texto)
e agora sim:

01/03/2018 12:30
Perfeito! Até agora aprendemos a pegar a data atual com a classe date, datetime e até aprendemos a formatar datas, transformando-as em strings. Mas e se precisássemos fazer o caminho contrário?
"""
