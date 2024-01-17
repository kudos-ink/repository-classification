import json
import requests
import os
from urllib.parse import urlparse


token = os.getenv("GH_TOKEN")

with open("dapps_input.json", "r") as file:
    urls = [line["repository"].strip() for line in json.load(file)]

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
        languages = requests.get(repo_data["languages_url"], headers=headers).json()
        repo_info_list.append({
            "name": repo.split("/")[1],
            "repository_url": url,
            "interests": repo_data.get("topics"),
            "emoji": ""
        })
    else:
        print(f"Failed to fetch data for {repo}. Status code: {response.status_code}")

# Save the data to a JSON file
with open("dapps_output.json", "w", encoding="utf-8") as json_file:
    json.dump(repo_info_list, json_file, indent=2)
