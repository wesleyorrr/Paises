
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

servidor = r"DESKTOP-U4O9SM4\SQLEXPRESS"
banco = "Projeto_Paises"

parametros = quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={servidor};"
    f"DATABASE={banco};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(
    f"mssql+pyodbc:///?odbc_connect={parametros}"
)

query = """
SELECT
    Pais,
    Continente,
    Populacao_Milhoes,
    PIB_Trilhoes,
    IDH
FROM VW_Analise_Paises
"""

with engine.connect() as conexao:
    df = pd.read_sql(query, conexao)

print(df)
print("\nMédia do IDH:")
print(df["IDH"].mean())

print("\nPaíses ordenados pelo IDH:")
print(df.sort_values(by="IDH", ascending=False))

print("\nTotal de registros:", len(df))

engine.dispose()

media_idh = df["IDH"].mean()

paises_acima_media = df[df["IDH"] > media_idh]

print("\nPaíses com IDH acima da média:")
print(paises_acima_media[["Pais", "IDH"]])

paises_abaixo_media = df[df["IDH"] < media_idh]

print("\nPaíses com IDH abaixo da média:")
print(paises_abaixo_media[["Pais", "IDH"]])

print("\nQuantidade de países acima da média:")
print(len(paises_acima_media))

print("\nQuantidade de países abaixo da média:")
print(len(paises_abaixo_media))

print("\nMédia do IDH por continente:")

media_continente = df.groupby("Continente")["IDH"].mean()

print(media_continente)

print("\nPaís com maior IDH por continente:")

maior_idh_continente = df.loc[
    df.groupby("Continente")["IDH"].idxmax(),
    ["Continente", "Pais", "IDH"]
]

print(maior_idh_continente)


print("\nRanking de IDH por continente:")

ranking_continentes = df.sort_values(
    by=["Continente", "IDH"],
    ascending=[True, False]
)

print(ranking_continentes[["Continente", "Pais", "IDH"]])

print("\nPIB médio por continente:")

pib_medio_continente = df.groupby("Continente")["PIB_Trilhoes"].mean()

print(pib_medio_continente.round(2))


print("\nPopulação total por continente:")

populacao_continente = df.groupby("Continente")["Populacao_Milhoes"].sum()

print(populacao_continente)

print("\nResumo econômico por continente:")

resumo_continentes = df.groupby("Continente").agg({
    "Populacao_Milhoes": "sum",
    "PIB_Trilhoes": "mean"
})

print(resumo_continentes.round(2))

print("\nContinente com maior PIB médio:")

maior_pib = resumo_continentes[
    "PIB_Trilhoes"
].idxmax()

print(maior_pib)

print("\nContinente com menor PIB médio:")

menor_pib = resumo_continentes[
    "PIB_Trilhoes"
].idxmin()

print(menor_pib)


print("\nRanking do PIB médio por continente:")

ranking_pib = resumo_continentes.sort_values(
    by="PIB_Trilhoes",
    ascending=False
)

print(ranking_pib)

print("\nRanking do PIB médio por continente:")

ranking_pib = resumo_continentes.sort_values(
    by="PIB_Trilhoes",
    ascending=False
)

print(ranking_pib)

print("\nParticipação percentual do PIB médio:")

total_pib = resumo_continentes["PIB_Trilhoes"].sum()

participacao_pib = (
    resumo_continentes["PIB_Trilhoes"] / total_pib
) * 100

print(participacao_pib.round(2))


print("\nValidação dos percentuais:")

print("Total:", participacao_pib.sum().round(2), "%")

df_excel = pd.read_excel(
    "dados/Paises.xlsx",
    sheet_name="Bases",
    header=0
)
print("\nIniciando tratamento dos dados:")

# Remover espaços extras dos nomes das colunas
df_excel.columns = df_excel.columns.str.strip()

# Remover espaços extras dos campos de texto
colunas_texto = df_excel.select_dtypes(include="str").columns

for coluna in colunas_texto:
    df_excel[coluna] = df_excel[coluna].str.strip()

# Verificar valores ausentes
print("\nValores ausentes:")
print(df_excel.isnull().sum())

# Verificar registros duplicados
print("\nRegistros duplicados:")
print(df_excel.duplicated().sum())

# Verificar tipos de dados
print("\nTipos de dados:")
print(df_excel.dtypes)

excel = pd.ExcelFile("dados/Paises.xlsx")

print("\nAbas encontradas no Excel:")
print(excel.sheet_names)

for aba in excel.sheet_names:
    print(f"\nConteúdo inicial da aba: {aba}")

    previa = pd.read_excel(
        excel,
        sheet_name=aba,
        header=None,
        nrows=10
    )

    print(previa)
    
    print("\nColunas da base tratada:")

print(df_excel.columns.tolist())

df_excel.columns = [
    "Pais",
    "Continente",
    "Populacao_Milhoes",
    "PIB_Trilhoes",
    "Area_Km2",
    "Expectativa_Vida",
    "IDH",
    "Moeda",
    "Capital"
]

print("\nColunas padronizadas:")
print(df_excel.columns.tolist())


df_excel["Populacao_Milhoes"]
print("\nConferência final da base:")

print("Quantidade de linhas:", len(df_excel))
print("Quantidade de colunas:", len(df_excel.columns))

print("\nPrimeiros registros:")
print(df_excel.head())

print("\nTipos de dados da base tratada:")
print(df_excel.dtypes)

print("\nValidação dos valores numéricos:")

print("População menor ou igual a zero:",
      (df_excel["Populacao_Milhoes"] <= 0).sum())

print("PIB negativo:",
      (df_excel["PIB_Trilhoes"] < 0).sum())

print("Área menor ou igual a zero:",
      (df_excel["Area_Km2"] <= 0).sum())

print("IDH fora do intervalo de 0 a 1:",
      (~df_excel["IDH"].between(0, 1)).sum())