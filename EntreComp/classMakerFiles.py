import csv
import json
import os
import base64

# Function to create a Data URI for an SVG image
def encode_image_to_data_uri(svg_content):
    if svg_content:
        # Encode SVG content to base64
        encoded_svg = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
        return f"data:image/svg+xml;base64,{encoded_svg}"
    return None

# Function to create JSON structure for badge class
def create_badge_class_json(row):
    image_data_uri = encode_image_to_data_uri(row["Level Icon SVG Text"])
    return {
        "id": f"https://bloom.pm/badges/{row['Short Name']}",
        "type": "BadgeClass",
        "name": row["Level"],
        "description": row["LevelDescription"],
        "image": image_data_uri or "Default image URL if no SVG provided",  # Provide a fallback URL if no SVG content
        "criteria": {
            "narrative": row["Levels Text"],
        },
        "issuer": {
            "id": "https://bloom.pm",
            "name": "Bloom.pm",
            "url": "https://bloom.pm/wordpress/wp-content/uploads/badges/issuer.json",
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
