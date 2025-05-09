print('Python na Escola de Programação da Alura')

nome = 'André'
idade = 26

print(f'Meu nome é {nome} e tenho {idade} anos')

print(
'''
A
L
U
R
A
''')

pi = 3.14159

print(f'O valor de pi arredondado é {pi:.2f}')


# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))


pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))



#numero = int(input("Digite um número: "))
#if numero % 2 == 0:
#    print("O número é par.")
#else:
#    print("O número é ímpar.")