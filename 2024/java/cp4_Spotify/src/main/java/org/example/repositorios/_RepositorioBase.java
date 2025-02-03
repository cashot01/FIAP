package org.example.repositorios;

import org.example.entidades._EntidadeBase;

import java.util.ArrayList;

public interface _RepositorioBase <T extends _EntidadeBase>{
    void cadastrar(T objeto);
    void atualizar(T objeto);
    void deletar(T objeto);
    ArrayList<T> listar();
}
