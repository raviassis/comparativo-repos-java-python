import requests

class Repository:
    def __init__(self, token):
        self.token = token
    
    def __get_query(self, primaryLanguage):
        query = f"""
        {{
            search(
            query:"primarylanguage:{primaryLanguage} stars:>0 sort:stars", 
            type:REPOSITORY, 
            first:100,
            ) {{
            pageInfo {{
                startCursor
                endCursor
                hasPreviousPage
                hasNextPage
            }}
            edges {{
                node {{
                ... on Repository {{
                    nameWithOwner
                    primaryLanguage {{
                    name
                    }}
                    stargazers {{
                    totalCount
                    }}
                }}
                }}
            }}
            }}
        }}
        """
        return query

    def get_repositories(self, primaryLanguage, num_repositories):
        headers = headers = {'Authorization': f'Bearer {self.token}'}
        repositories = list()
        query = self.__get_query(primaryLanguage)
        result = requests.post("https://api.github.com/graphql", json={'query': query}, headers=headers)
        if result.status_code == 200:
            data = result.json()['data']['search']
            repositories = list(map(lambda x: x['node'], data['edges']))
            print(f"\rRetrieve {len(repositories)} repositories", end = '')
            return repositories 
            
