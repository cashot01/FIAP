package org.example.repositorios;

import org.example.entidades._EntidadeBase;

import java.util.ArrayList;

public class RepositorioBaseImp<T extends _EntidadeBase> implements _RepositorioBase<T> {
    protected ArrayList<T> lista = new ArrayList<>();

    @Override
    public void cadastrar(T objeto) {
        lista.add(objeto);
    }

    @Override
    public void atualizar(T objeto) {
        var objetoDesatualizado = lista.stream()
                .filter(item -> item.getId() == objeto.getId())
                .findFirst();
        lista.remove(objetoDesatualizado);
        lista.add(objeto);

    }

    @Override
    public void deletar(T objeto) {
        lista.remove(objeto);

    }

    @Override
    public ArrayList<T> listar() {
        return lista;
    }
}
