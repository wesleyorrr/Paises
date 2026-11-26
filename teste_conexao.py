
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