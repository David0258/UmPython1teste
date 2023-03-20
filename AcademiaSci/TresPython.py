alunos_notas = [{"Nome": str, "Notas": []}]


def calcula_media(notas: []) -> float:
    return sum(notas) / 4


while True:
    nome_aluno = input('Informe o nome do aluno: ')

    notas_aluno = []
    for i in range(4):
        notas_aluno.append(float(input(f'Insira a {i + 1}ª nota: ')))

    alunos_notas.append({"Nome": nome_aluno, "Notas": notas_aluno})

    sair = input('Deseja sair (responda com sim/nao): ')
    if sair.lower().strip() == 's' or sair.lower().strip() == 'sim':
        break

alunos_notas.pop(0)
print()

for notas_aluno in alunos_notas:
    print(f'\nAluno: {notas_aluno["Nome"]}')
    media = round(calcula_media(notas_aluno["Notas"]), 1)

    if media < 6:
        print(f'Média: {media} | REPROVADO')
    else:
        print(f'Média: {media} | APROVADO')
