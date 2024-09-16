package fiap.tds.repositories;

import java.util.List;

public interface _CrudRepositorio<T> {
    void Insert(T entity);
    void Update(T entity);
    void Delete(int id);
    T GetById(int id);
    List<T> GetAll();
}
