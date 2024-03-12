import csv
import json
import os

# Function to create JSON structure for badge class
def create_badge_class_json(row):
    return {
        "id": f"https://bloom.pm/badges/{row['Short Name']}",
        "type": "BadgeClass",
        "name": row["Level"],
        "description": row["LevelDescription"],
        "image": row["Level Icon SVG Text"],  # Update this if you have a direct URL to the badge image
        "criteria": {
            "narrative": row["Levels Text"],
        },
        "issuer": {
            "id": "https://bloom.pm",
            "name": "Bloom.pm",
            "url": "https://bloom.pm",
            "email": "bilal@bloom.pm"
        },
        "tags": [row["Short Name"], "community", "self-recognition"]
    }

# Function to process CSV and generate JSON files
def process_csv_and_generate_json(csv_file_path, output_dir):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            badge_class_json = create_badge_class_json(row)
            filename = f"{row['Short Name']}.json"
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as jsonfile:
                json.dump(badge_class_json, jsonfile, indent=4)

# Specify your CSV file path and output directory
csv_file_path = './classes.csv'
output_dir = './'

# Process CSV and generate JSON files
process_csv_and_generate_json(csv_file_path, output_dir)
