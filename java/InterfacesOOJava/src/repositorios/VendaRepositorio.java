package repositorios;

import entidades.Venda;

import java.util.ArrayList;

public class VendaRepositorio implements Cadastro{
    ArrayList<Venda> listaVendas = new ArrayList<Venda>();
    @Override
    public void adicionar(Object novoObjeto) {
        listaVendas.add((Venda) novoObjeto);

    }

    @Override
    public void remover(Object objeto) {
        listaVendas.remove(objeto);

    }

    @Override
    public Object listar() {
        return null;
    }

    @Override
    public void alterar(Object objeto) {

    }
}
