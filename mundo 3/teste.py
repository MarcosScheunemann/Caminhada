sequence = str(input('Digite o teste: '))


def solution(sequence):
    lista = []
    for x in sequence:
        if x in "([{":
            lista += [x]
        elif x in ")]}":
            if len(lista) < 1:
                return False
            elif lista[-1] == "{" and x == "}":
                lista.pop()
            elif lista[-1] == "[" and x == "]":
                lista.pop()
            elif lista[-1] == "(" and x == ")":
                lista.pop()

    if len(lista) == 0:
        return True
    else:
        return False


print(solution(sequence))

