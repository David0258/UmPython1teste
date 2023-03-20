numeros = []

media = 0
pares = []
impares = []


def is_par(numero):
    return (numero % 2) == 0


def extract_pares_impares():
    global numeros
    global pares
    global impares

    for n in numeros:
        if is_par(n):
            pares.append(n)
        else:
            impares.append(n)


def calcula_media():
    global numeros
    global media

    media = sum(numeros) / 5


for i in range(5):
    numeros.append(int(input('Insira um número: ')))


extract_pares_impares()
calcula_media()

print(f'Números pares: {pares}\n')
print(f'Números ímpares: {impares}\n')

print(f'Média dos números: {media}')

print('Fim.')