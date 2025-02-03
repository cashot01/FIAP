package repositorio;

import java.util.List;
import java.util.Optional;

public interface _RepositorioBase<T> {
    void Insert(T entity);
    void Update(T entity, int id);
    void Delete(int id);
    Optional<T> GetById(int id);
    List<T> GetAll();
}
