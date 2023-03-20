numeros = []
numero_maior = 0
numero_menor = 0


for i in range(5):
    numeros.append(int(input('Insira o valor: ')))


numero_maior = max(numeros)
print(f'O maior valor é: {numero_maior}')
numero_menor = min(numeros)
print(f'O menor valor é: {numero_menor}')

