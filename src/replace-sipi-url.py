import os
import json

def replace_url_in_json_files(directory, old_url, new_url):
    """
    This function searches through all JSON files in a given directory
    and replaces the specified old URL with the new URL.

    :param directory: The directory containing JSON files.
    :param old_url: The URL to be replaced.
    :param new_url: The new URL to replace the old one.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            file_path = os.path.join(directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)

                # Recursively replace all occurrences of the old URL in the JSON object
                def replace_urls(obj):
                    if isinstance(obj, dict):
                        for key, value in obj.items():
                            if isinstance(value, (dict, list)):
                                replace_urls(value)
                            elif isinstance(value, str) and old_url in value:
                                obj[key] = value.replace(old_url, new_url)
                    elif isinstance(obj, list):
                        for item in obj:
                            replace_urls(item)

                replace_urls(data)

                # Write the modified data back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(data, file, indent=4)

            except Exception as e:
                print(f"An error occurred while processing {file_path}: {e}")

# Project identifier and directory path
project = '0801'
directory = os.path.join(os.path.dirname(__file__), '..', 'data', project)
old_url = 'http://iiif.dasch.swiss/'
new_url = 'https://iiif.dasch.swiss/'

replace_url_in_json_files(directory, old_url, new_url)
