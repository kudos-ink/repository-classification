import json
import yaml
import os

interests_file = os.environ.get("INTERESTS_JSON", "data/interests.json")
# Load the JSON data from the file
with open(interests_file, 'r') as json_file:
    data = json.load(json_file)

# Extract the "value" list from the JSON data
value_list = [interest['value'] for interest in data['interests']]

# Load the existing YAML file
with open('.github/ISSUE_TEMPLATE/NEW_PROJECT.yaml', 'r') as yaml_file:
    existing_yaml_data = yaml.safe_load(yaml_file)

# Update the "options" list in the YAML file with the new "value" list
existing_yaml_data['body'][2]['attributes']['options'] = value_list

# Write the updated YAML data back to the file
with open('.github/ISSUE_TEMPLATE/NEW_PROJECT.yaml', 'w') as updated_yaml_file:
    yaml.dump(existing_yaml_data, updated_yaml_file)
