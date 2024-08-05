package repositorios;

public interface Cadastro {
    void adicionar(Object novoObjeto);
    void remover(Object objeto);
    Object listar();
    void alterar(Object objeto);
}
