
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

print("\nIniciando tratamento dos dados:")

# Remover espaços extras dos nomes das colunas
df_excel.columns = df_excel.columns.str.strip()

# Remover espaços extras dos campos de texto
colunas_texto = df_excel.select_dtypes(include="object").columns

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
