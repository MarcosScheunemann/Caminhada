n1 = int(input('Digite um número:'))
n2 = int(input('Digite mais um número'))
s = n1 + n2
print('A soma entre {} e {}, vale {}'.format(n1, n2, s))
# o formato acima é melhor que o visto ao lado por ser mais organizado:  print('A soma entre', n1, "e", n2, 'vale', s)


n3 = input('digite algo:')
print("esta frase é {}".format(type(n3)))
print("É um número? {}".format(n3.isnumeric()))
print("É alfabético?", n3.isalpha())
print("É minúscula?", n3.islower())
print("É maiúscula?", n3.isupper())
print("contém somente espaços?", n3.isspace())
