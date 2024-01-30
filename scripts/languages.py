import json
import os

lang_file = os.environ.get("LANGUAGES_JSON", "data/languages.json")
repo_full_file = os.environ.get("REPOSITORY_FULL_JSON", "data/repository_full.json")

# Read existing languages.json file if it exists
existing_languages = []
with open(lang_file, 'r', encoding='utf-8') as existing_file:
    existing_languages = json.load(existing_file)["languages"]

# Read the JSON file
with open(repo_full_file, 'r') as file:
    data = json.load(file)

# Extract languages from the data
repositories = data.get('repositories', [])
new_languages = [language for repo in repositories for language in repo.get('languages', [])]

# Identify new languages not already in existing_languages
new_languages_set = set(new_languages) - set(lang['value'] for lang in existing_languages)

# Create a new structure for new languages
new_languages_info = [{'value': lang.lower(), 'label': lang.title(), 'emoji': '🦀'} for lang in new_languages_set]

# Append new languages to existing_languages
updated_languages = dict(languages=existing_languages + new_languages_info)

# Save the updated structure to languages.json
with open(lang_file, 'w') as output_file:
    json.dump(updated_languages, output_file, ensure_ascii=False, indent=2)

print(f"Languages information updated and saved to '{lang_file}'")
