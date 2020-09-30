from dotenv import load_dotenv, find_dotenv
import os
import json
import pandas as pd
from repositories import Repository

load_dotenv(find_dotenv())

repository = Repository(os.getenv("TOKEN"))
print("Get Java Repositories")
repositoriesJava = repository.get_repositories("java", 100)
print("\nGet Python Repositories")
repositoriesPython = repository.get_repositories("python", 100)
repositories = repositoriesJava + repositoriesPython
df = pd.json_normalize(repositories)
csvText = df.to_csv().replace("\r", "")
filename = "repositories.csv"
print(f"Write repositories on file {filename}")
file = open(filename, "w")
file.write(csvText)
file.close()
print("End script")