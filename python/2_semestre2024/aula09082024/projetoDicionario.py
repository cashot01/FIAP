import os
os.system("cls")



notas ={
    "Joao" : 9.5,
    "Maria": 10.0,
    "José": 5
}

def menu():
    print("""
    0 - sair 
    1 - Adicionar novo aluno
    2 - editar aluno | Nota
    3 - listar alunos
    4 - excluir aluno
    5 - calcular media da turma
    6 - consultar aluno
    7 - apagar toda sala """)

    escolha = input("Escolha: ")
    while not escolha.isdigit() or int(escolha) < 0 or int(escolha) > 7:
        os.system("cls")
        print("opção invalida ")
        menu()
        escolha = input("Escolha: ") 

    escolha = int(escolha)
    match escolha:
        case 0:
            sair()
        case 1:
            adicionarAluno()
        case 2:
            editarAluno()
        case 3:
            listarAlunos()
        case 4:
            excluirAluno()
        case 5: 
            calcularMediaTurma()
        case 6:
            consultarAluno()
        case 7:
            apagarSala()

def sair():
    os.system("cls")
    print("saindo ")

# def notaValida(n: float) -> bool:



def adicionarAluno():

    input("Voltar menu...")
    os.system("cls")
    menu()







menu()