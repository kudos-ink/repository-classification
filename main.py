import json
import requests
import os
from urllib.parse import urlparse


token = os.getenv("GH_TOKEN")

with open("repository_urls.txt", "r") as file:
    urls = [line.strip() for line in file]

headers = {
    "Authorization": f"Bearer {token}",
    "X-GitHub-Api-Version": "2022-11-28",
    "Accept": "application/vnd.github+json"
}

repo_info_list = []


for url in urls:
    path_components = urlparse(url).path.split("/")
    if len(path_components) == 3:
        repo = f"{path_components[1]}/{path_components[2]}"
    else:
        print(f"Invalid GitHub URL format: {url}")
        continue
    url = f"https://api.github.com/repos/{repo}"
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_data = response.json()
        
        repo_info_list.append({
            "Repository": repo,
            "About": repo_data.get("description", ""),
            "Topics": repo_data.get("topics")
        })
    else:
        print(f"Failed to fetch data for {repo}. Status code: {response.status_code}")

# Save the data to a JSON file
with open("repository_info.json", "w", encoding="utf-8") as json_file:
    json.dump(repo_info_list, json_file, indent=2)
