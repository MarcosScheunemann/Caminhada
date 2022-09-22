"""
Cores no Terminal:

\033[*****m      => inicio para por um código de cor
\033[estilo : texto : fundo   m
\033[0:33:44m    => exemplo de cor

"""

print('\033[0;30;41mOlá Mundo\033[m')
print('\033[4;33;44mOlá Mundo\033[m')
print('\033[1;33;43mOlá Mundo\033[m')
print('\033[30;42mOlá Mundo\033[m')
print('\033[mOlá Mundo\033[m')
print('\033[7;30mOlá Mundo\033[m')

print('Os valores são \033[0;30;41m{}\033[m e \033[7;30m{}\033[m!!!'.format(3, 5))

print('Os valores são {}{}{} e {}{}{}!!!'.format('\033[0;30;41m', 3, '\033[m', '\033[7;30m', 5, '\033[m'))
