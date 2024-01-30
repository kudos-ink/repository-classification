import json
import os

repo_file = os.environ.get("REPOSITORY_JSON", "data/repository.json")

# Read the JSON file
with open(repo_file, "r", encoding="utf-8") as file:
    data = json.load(file)

# Repositories to keep at the top without a specific order
top_repositories = ["Polkadot SDK"]

# Separate the repositories into two lists: top repositories and the rest
top_repo_list = [repo for repo in data["repositories"] if repo["name"] in top_repositories]
rest_repo_list = [repo for repo in data["repositories"] if repo["name"] not in top_repositories]

# Sort the rest of the repositories by name
rest_repo_list.sort(key=lambda x: x["name"])

# Combine the top repositories and the sorted rest of the repositories
sorted_repositories = top_repo_list + rest_repo_list

# Update the data with the sorted repositories
data["repositories"] = sorted_repositories


# Save the modified data to a new JSON file
with open(repo_file, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
