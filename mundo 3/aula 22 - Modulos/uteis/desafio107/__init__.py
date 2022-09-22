def metade(n, moed=False):
    n = n/2
    if moed:
        n = moeda(n)
    return n


def dobro(n, moed=False):
    n *= 2
    if moed:
        n = moeda(n)
    return n


def aumentar(n, p, moed=False):
    resultado = n * ((p/100) + 1)
    if moed:
        resultado = moeda(resultado)
    return resultado


def diminuir(n, p, moed=False):
    resultado = n - (p/100) * n
    if moed:
        resultado = moeda(resultado)
    return resultado


def moeda(m):
    return f'R${m:.2f}'.replace(".",",")


def resumo(n, a, d):
    print('-' * 40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-' * 40)
    print(f'{"Preço analisado:":<30}', end="")
    print(moeda(n))
    print(f'{"Dobro do preço:":<30}', end="")
    print(dobro(n, True))
    print(f'{"Metade do preço:":<30}', end="")
    print(metade(n, True))
    print(f'{f"{a}% de aumento":<30}', end="")
    print(aumentar(n, a, True))
    print(f'{f"{d}% de redução:":<30}', end="")
    print(diminuir(n, d, True))
    print('-' * 40)

