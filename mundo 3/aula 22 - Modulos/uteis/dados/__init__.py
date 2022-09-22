def leiaDinheiro(frase):
    while True:
        n = input(f'{frase}').replace(",", ".").strip()
        if n.isalpha() or n == "":
            print(f'\033[0;31mERRO: "{n}" é um preço inválido! \033[m')
        elif not n.replace('.', '').isnumeric():
            print(f'\033[0;31mERRO: "{n}" é um preço inválido! \033[m')
        else:
            n = float(n)
            n = f'{n:.2f}'
            return n.replace('.', ',')

