package Repositorios;

import Entidades._EntidadeBase;

import java.util.ArrayList;

public interface _RepositorioBase<T extends _EntidadeBase> {

    void cadastrar(T objeto);
    ArrayList<T> listar();
    void atualizar(T objeto);
    void deletar(T objeto);
    void deletarPorId(int id);

    // o default numa interface, é um método que já tem uma implementação padrão
    //TODO: implementar corretamente o default, pois o listar vai gastar muita memória
    default T buscarPorId(int id){
        return listar().stream().filter(x -> x.getId() == id).findFirst().orElse(null);
    }
}
