from repositories import Repository
from repositoryData import RepositoryData

def updateDataBase(token):
    repository = Repository(token)
    print("Get Java Repositories")
    repositoriesJava = repository.get_repositories("java", 100)
    print("Get Python Repositories")
    repositoriesPython = repository.get_repositories("python", 100)
    repositories = repositoriesJava + repositoriesPython
    RepositoryData().update(repositories)