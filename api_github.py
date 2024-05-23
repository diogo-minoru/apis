import requests
import pandas as pd

url = "https://api.github.com/search/repositories?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers = headers)
#print(f"Status code: {r.status_code}")

response_dict = r.json()

######################################################
# Explorando chaves do json
print(response_dict.keys())

######################################################
# Avaliando quantidade de repositórios
print(response_dict["total_count"])

######################################################
# Acessando os repositórios
repo_dicts = response_dict["items"]
print(repo_dicts)

######################################################
#Explorando o primeiro repositório

#repo_dict = repo_dicts[0]
#print(repo_dict)
#print(len(repo_dict))

#for key, value in sorted(repo_dict.items()):
#    print(key)

######################################################
# Armazenando os repositórios em um dataframe
columns = ["name", "stargazers_count", "html_url", "created_at", "updated_at", "description"]

data_frame_1 = pd.DataFrame(repo_dicts, columns = columns)
print(data_frame_1)
