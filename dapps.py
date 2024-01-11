import requests
import json
import os


# Make a GET request to the JSON file URL
json_url = os.environ.get("DAPPS_URL", "https://polkadot.network/page-data/sq/d/1260342618.json")
response = requests.get(json_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON content
    json_data = response.json()

    # Access the specific data you need from the JSON object
    all_file_edges = json_data.get("data", {}).get("allFile", {}).get("edges", [])

    # Filter entries where relativePath starts with "dapp"
    filtered_entries = [
        {
            "name": os.path.basename(entry["node"]["relativePath"]).split(".")[0],
            "repository": ""  # Empty repository key
        }
        for entry in all_file_edges
        if entry["node"]["relativePath"].startswith("dapp")
    ]

    # Create a new JSON file with the filtered entries
    new_json_filename = "dapps.json"

    with open(new_json_filename, "w") as new_json_file:
        json.dump(filtered_entries, new_json_file, indent=2)

    print(f"Filtered relativePaths saved to {new_json_filename}")
else:
    print("Failed to retrieve the JSON file. Status code:", response.status_code)
