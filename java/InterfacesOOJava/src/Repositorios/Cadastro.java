package Repositorios;

import Entidades._EntidadeBase;

import java.util.ArrayList;

public interface Cadastro<T extends _EntidadeBase> {
    void cadastrar(T objeto);
    ArrayList<T> listar();
    void atualizar(T objeto);
    void deletar(T objeto);
}
