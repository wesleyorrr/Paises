
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
print("\nTotal de registros:", len(df))

engine.dispose()
