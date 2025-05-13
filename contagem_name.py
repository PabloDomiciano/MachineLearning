import pandas as pd

conversao = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 0,
}


def carregar_dados(caminho_csv):
    return pd.read_csv(caminho_csv)


def converter_notas(df, coluna_nota='nota', nova_coluna='nota_numerica', mapa=conversao):
    df[nova_coluna] = df[coluna_nota].map(mapa)
    return df


def calcular_estatisticas(df, coluna_nome='nome', coluna_nota='nota_numerica', coluna_disciplina='disciplina'):
    contagem = df[coluna_nome].value_counts()

    disciplinas = {}

    for index, row in df.iterrows():
        disciplina = row[coluna_disciplina]
        nota = row[coluna_nota]

        if disciplina not in disciplinas:
            disciplinas[disciplina] = {'total': 0, 'count': 0}

        disciplinas[disciplina]['total'] += nota
        disciplinas[disciplina]['count'] += 1

    media_disciplina = {}
    for disciplina, dados in disciplinas.items():
        media_disciplina[disciplina] = dados['total'] / dados['count']

    return contagem, media_disciplina


def main():
    df = carregar_dados('fake_names.csv')

    df = converter_notas(df)

    contagem, media_disciplina = calcular_estatisticas(df)

    print("Contagem por nome:")
    print("---------------------")
    print(contagem)
    print("---------------------")
    print(f"\nMédia das notas por disciplina:")
    print("------------------------------------")
    print('\n', media_disciplina)


if __name__ == '__main__':
    main()
