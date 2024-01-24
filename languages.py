import json

# Read existing languages.json file if it exists
existing_languages = []
try:
    with open('languages.json', 'r', encoding='utf-8') as existing_file:
        existing_languages = json.load(existing_file)
except FileNotFoundError:
    pass

# Read the JSON file
with open('repository_full.json', 'r') as file:
    data = json.load(file)

# Extract languages from the data
repositories = data.get('repositories', [])
new_languages = [language for repo in repositories for language in repo.get('languages', [])]

# Identify new languages not already in existing_languages
new_languages_set = set(new_languages) - set(lang['value'] for lang in existing_languages)

# Create a new structure for new languages
new_languages_info = [{'value': lang.lower(), 'label': lang.title(), 'emoji': '🦀'} for lang in new_languages_set]

# Append new languages to existing_languages
updated_languages = existing_languages + new_languages_info
# Save the updated structure to languages.json
with open('languages.json', 'w') as output_file:
    json.dump(updated_languages, output_file, ensure_ascii=False, indent=2)

print("Languages information updated and saved to 'languages.json'")
