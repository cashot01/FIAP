package org.example.repositorios;

import java.util.List;
import java.util.Optional;

public interface _CrudRepositorio<T> {
    void Cadastrar(T entidade);

    void Atualizar(T entidade, int id);

    void Deletar(int id);

    Optional<T> BuscarPorId(int id);

    List<T> Listar();
}
