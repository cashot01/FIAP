package Repositorios;

import Entidades._EntidadeBase;

import java.util.ArrayList;

public abstract class _RepositorioBaseImpl<T extends _EntidadeBase> implements _RepositorioBase<T> {

    protected ArrayList<T> lista = new ArrayList<>();

    @Override
    public void cadastrar(T objeto) {
        lista.add(objeto);
    }

    @Override
    public ArrayList<T> listar() {
        return lista;
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
        lista.remove(objeto);
    }

    @Override
    public void deletarPorId(int id) {
        var objetoRemovido = lista.stream().filter(x -> x.getId() == id).findFirst().get();
        lista.remove(objetoRemovido);
    }
}
