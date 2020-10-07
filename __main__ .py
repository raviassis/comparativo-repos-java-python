from dotenv import load_dotenv, find_dotenv
import os
from updatedatabase import updateDataBase
from exportdatatocsv import exportDataToCsv
from analyzerepository import AnalisysRepository
from repositoryData import RepositoryData

load_dotenv(find_dotenv())
token = os.getenv("TOKEN")

print("Options")
print("1 - Update repositories data base")
print("2 - Export repositories data base to csv")
print("3 - Analyze repositories")
op = input()
if op == '1':
    updateDataBase(token)
elif op == '2':
    exportDataToCsv()
elif op == '3':
    repositories = RepositoryData().get()
    for repo in repositories:
        try:
            analiser = AnalisysRepository(repo['url'])
            result = analiser.analyze()
            repo['loc_data'] = result
            RepositoryData().update(repositories)
        except:
            print("Couldn't analyze the repository " + repo['nameWithOwner'])
else:
    print("Invalid option!")