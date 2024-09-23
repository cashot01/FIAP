import oracledb
import pandas as pd

# conectando banco dados
try:
    # efetua a conexão com usuario
    conn = oracledb.connect(user="RM555466", password="071105", dsn="oracle.fiap.com.br:1521/ORCL")
except:
    print("Não efetuou conexão")
else:
    print("Conexão efetuada com sucesso")