package _1_Introducao_a_classes.models;

public class Aluno {
    public String nome;
    public String matricula;
    public String dataDeNascimento;
    public boolean ativo;
    public int numeroDeDps;
    public int numeroDeFaltas;

    public void matricular(String disciplina){
        System.out.println(
                "Matriculando o aluno a disciplina de "
                        + disciplina );
    }
}
