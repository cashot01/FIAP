package Repositorios;

import Entidades._EntidadeBase;

import java.util.ArrayList;

public class _RepositorioBaseImpl<T extends _EntidadeBase> implements _RepositorioBase<T>{
    ArrayList<T> lista = new ArrayList<>();
    @Override
    public void cadastrar(T objeto) {

    }

    @Override
    public ArrayList<T> listar() {
        return null;
    }

    @Override
    public void atualizar(T objeto) {
        // atualizar objeto por id
        var objetoAtualizado = lista.stream().filter(x -> x.getId() == objeto.getId()).findFirst().get();
        lista.remove(objetoAtualizado);
        lista.add(objeto);

    }

    @Override
    public void deletar(T objeto) {
        var objetoRemovido = lista.stream().filter(x -> x.getId() == objeto.getId()).findFirst().get();
        lista.remove(objetoRemovido);
    }

    @Override
    public void deletarPorId(T objeto) {

    }
}
