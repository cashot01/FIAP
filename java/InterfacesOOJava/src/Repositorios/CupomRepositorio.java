package Repositorios;

import Entidades.Cupom;

import java.util.ArrayList;
import java.util.Objects;

public class CupomRepositorio extends _RepositorioBaseImpl<Cupom>{
    public void deletarPorCodigo(String codigo){
        var cupom = lista.stream().filter(c -> Objects.equals(c.getCodigo(), codigo))
    }
}
