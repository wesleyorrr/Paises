
import pyodbc

servidor = r"DESKTOP-U4O9SM4\SQLEXPRESS"
banco = "Projeto_Paises"

conexao = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={servidor};"
    f"DATABASE={banco};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

print("Conexão com SQL Server realizada com sucesso!")

cursor = conexao.cursor()
cursor.execute("SELECT COUNT(*) FROM Paises")

total = cursor.fetchone()[0]

print(f"Total de países encontrados: {total}")

conexao.close()
