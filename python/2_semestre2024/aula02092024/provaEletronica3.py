# Estrutura da Prova inicial (3 questões)
prova = { 
    'Pergunta 1':
    { 
        'enunciado': 'Quanto é 2+2? ',
        'alternativas':
        { 
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'correta': 'b',
    },
    'Pergunta 2':
    {
        'enunciado': 'Quanto é 3x2? ',
        'alternativas':
        {
            'a': '4',
            'b': '101',
            'c': '6',
        },
        'correta': 'c',
    },
    'Pergunta 3':
    {
        'enunciado': 'Qual o cubo de 2? ',
        'alternativas':
        {
            'a': '4',
            'b': '8',
            'c': '16',
        },
        'correta': 'b',
    },
}

# Estrutura para gravas as notas
turma = []

# Procedimento que adiciona uma questão na prova
# Parâmetro: p | prova (dict)
def add_questao(p: dict) -> None:
    # Lê os dados da pergunta adicionados pelo usuário
    descr_pergunta = input("\nEnunciado: ")
    alternativa_a = input("a) ")
    alternativa_b = input("b) ")
    alternativa_c = input("c) ")
    alternativa_correta = input("Alternativa correta: ")
    # Grava os dados na pergunta
    p[f'Pergunta {len(prova) + 1}'] = { # 
        'enunciado': descr_pergunta,
        'alternativas': {
            'a': alternativa_a,
            'b': alternativa_b,
            'c': alternativa_c,
        },
        'correta': alternativa_correta,
    }

# Exibe o menu da aplicação
# Parâmetro: None
def exibe_menu():
    print("MENU\n----\n")
    print("0 - SAIR")
    print("1 - Realizar a prova")
    print("2 - Adicionar questão")
    print("3 - Listar provas executadas | média dos alunos ")


# Procedimento que Exibe a listagem dos alunos e calcula a média da turma
# Parâmetro: t | Turma (List)
def exibe_relatorio(t: list) -> None:
    soma_nota = 0
    print("\nNOME    NOTA")
    print("------------")
    for i in range(len(t)):
        print(f"{t[i]['nome']} \t{t[i]['nota']} ")
        soma_nota += t[i]['nota']
    print(f"\nMédia da turma: {soma_nota / len(t)}")
    
# Procedimento que grava a prova na turma
# Parâmetro: t | Turma (list)
# Parâmetro: nome | Nome que será gravado (str)
# Parâmetro: nota | nota que será gravada (float)
def grava_prova_aluno(t: list, nome: str, nota: float) -> None:
    aluno = {
        'nome': nome,
        'nota': nota
    }
    t.append(aluno.copy())

# Programa principal
import os
proxima_pergunta = 4
while True:
    os.system("cls")
    exibe_menu()
    escolha = input("\nEscolha: ")
    match escolha:
        case '0':
            break
        case '1':
            nome = input("\nNome do aluno: ")
            respostas_certas = 0
            # Exibindo as perguntas e enunciado
            for pergunta, dados_pergunta in prova.items():
                print(f'\n{pergunta}: \n\t{dados_pergunta["enunciado"]}')

                # Exibindo as alternativas
                for resposta, dados_resposta in dados_pergunta['alternativas'].items():
                    print(f'\t\t{resposta}) {dados_resposta}')

                # Lê a respost do usuário
                resposta_usuario = input('\nSua resposta: ')

                # verifica se acertou ou não
                if resposta_usuario == dados_pergunta['correta']:
                    print("Resposta CORRETA! :]\n")
                    respostas_certas += 1
                else:
                    print("Resposta INCORRETA! :,[\n")

            # mostra a nota
            quantidade_perguntas = len(prova)
            porcentagem_acerto = respostas_certas / quantidade_perguntas * 10
           
            print(f'\nVoce tirou nota {porcentagem_acerto}.')

            grava_prova_aluno(turma, nome, porcentagem_acerto)

            print("Dados gravados na Tabela com sucesso!")
        case '2':
            add_questao(prova)
        case '3':
            exibe_relatorio(turma)
        case _ : 
            print("Opção inválida!")
    input("\nDigite algo para continuar...")
            

