using TDSPG.API.Domain.Entity;

namespace TDSPG.API.Infrastructure.Persistence.Repositories
{
    public interface IRepository<T> where T : class
    {
        Task<T> GetByIdAsync(Guid id);
        Task<IEnumerable<T>> GetAsync();
        Task AddAsync(T establishment);
        Task UpdateAsync(T establishment);
        Task DeleteAsync(int id);
    }
}
