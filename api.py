import requests
from icecream import ic

api_url = "https://api.github.com"
username = input("github uername: ")

headers = {
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "maximbalan"
}

repos_url = f"{api_url}/users/{username}/repos"

r = requests.get(repos_url, headers=headers)

if r.status_code == 200:
    repositories = r.json()
    ic(f"Repos for {username}: ")
    for repo in repositories:
        repo_name = repo["name"]
        repo_description = repo["description"]
        ic("Repo: ", repo_name)
        ic("Description: ", repo_description)
else:
    ic("Error fetching repositories")