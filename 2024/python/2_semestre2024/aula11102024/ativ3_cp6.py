# INTEGRANTES: CAUAN ARANEGA S PASSOS RM555466, GUSTAVO R LAZZURI RM556772, LUCAS FIALHO RM557884

import os
os.system("cls") 
import oracledb

conn = oracledb.connect(user="RM555466", password="071105", dsn='oracle.fiap.com.br:1521/ORCL')
cursor = conn.cursor()

def main():
    
    
 
    while True:
        pk = input("Digite a PK: ")
        if pk.lower() == 'l':
            listar_registros(cursor)
            continue
        
        if pk == "0":
            print("programa finalizado")
            break
        try:
            pk = int(pk)
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
 
        cursor.execute("SELECT * FROM T_PESSOA_PY WHERE id = :id", {'id': pk})
        registro = cursor.fetchone()
 
        if registro:
            print(f"Registro encontrado: {registro}")
            acao = input("Deseja Editar (E) ou Excluir (X) o registro? ").lower()
 
            if acao == 'e':
                editar_registro(cursor, conn, pk, registro)
            elif acao == 'x':
                excluir_registro(cursor, conn, pk)
            else:
                print("Ação inválida.")
        else:
            cadastrar_registro(cursor, conn, pk)
 
def listar_registros(cursor):
    cursor.execute("SELECT * FROM T_PESSOA_PY")
    registros = cursor.fetchall()
    if registros:
        for registro in registros:
            print(registro)
    else:
        print("Nenhum registro encontrado.")
 
def cadastrar_registro(cursor, conn, pk):
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    email = input("Digite o email: ")
    telefone = input("Digite o telefone: ")
    endereco = input("Digite o endereço: ")
 
    cursor.execute("""
        INSERT INTO T_PESSOA_PY (id, nome, cpf, email, telefone, endereco)
        VALUES (:id, :nome, :cpf, :email, :telefone, :endereco)
    """, {'id': pk, 'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone, 'endereco': endereco})
    conn.commit()
    print("Registro cadastrado com sucesso.")
 
def editar_registro(cursor, conn, pk, registro):
    nome = input(f"Digite o nome [{registro[1]}]: ") or registro[1]
    cpf = input(f"Digite o CPF [{registro[2]}]: ") or registro[2]
    email = input(f"Digite o email [{registro[3]}]: ") or registro[3]
    telefone = input(f"Digite o telefone [{registro[4]}]: ") or registro[4]
    endereco = input(f"Digite o endereço [{registro[5]}]: ") or registro[5]
 
    cursor.execute('''
        UPDATE T_PESSOA_PY 
        SET nome = :nome, cpf = :cpf, email = :email, telefone = :telefone, endereco = :endereco
        WHERE id = :id
    ''', {'nome': nome, 'cpf': cpf, 'email': email, 'telefone': telefone, 'endereco': endereco, 'id': pk})
    conn.commit()
    print("Registro atualizado com sucesso.")
 
def excluir_registro(cursor, conn, pk):
    cursor.execute("DELETE FROM T_PESSOA_PY  WHERE id = :id", {'id': pk})
    conn.commit()
    print("Registro excluído com sucesso.")
 
if __name__ == "__main__":
    main()