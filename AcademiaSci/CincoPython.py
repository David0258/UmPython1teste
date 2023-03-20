import numpy

notas: list[list[float]] = []
alunos: list = []

for i in range(3):
    alunos.append(input(f'Informe o nome do(a) aluno(a) {i + 1}: '))
    notas_aluno = []
    for j in range(4):
        notas_aluno.append(float(input(f'Informe a {j + 1}ª nota: ')))

    notas.append(notas_aluno)

medias = []

for i in range(3):
    medias.append(sum(notas[i]) / 4)
    print()
    print(f'Aluno: {alunos[i]}')
    print(f'Média: {medias[i]}')

print(f'Maior media: {max(medias)} - {alunos[numpy.argmax(medias)]}')
print(f'Menor media: {min(medias)} - {alunos[numpy.argmin(medias)]}')