import os
import pandas as pd
from iiif_prezi3 import Manifest, Canvas, KeyValueString, ResourceItem, ExternalItem, ProviderItem, HomepageItem, config
from urllib.parse import urlparse

# Set auto_lang to English
config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

# Ensure 'manifests' directory exists
output_dir = 'data'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the CSV data into a DataFrame
csv_file_path = 'beol.csv'
data_frame = pd.read_csv(csv_file_path)

# Base URLs for components
manifest_server = 'https://iiif-manifest.dasch.swiss/' 
sipi_url = 'https://iiif.dasch.swiss/' 
base_ark = 'https://ark.dasch.swiss/ark:/72163/1/'
dsp_api = 'https://api.dasch.swiss/v2/'
project = '0801'  # The project identifier

# Define logo and provider details
dasch_logo = 'https://iiif.dasch.swiss/0810/7WumAIYuJsQ-CroJQljo3CV.jp2'
dasch_www = 'https://www.dasch.swiss/'
dasch_ror = 'https://ror.org/047f01g80'

# Initialise the Canvas index
canvas_index = 0

# Iterate through data and create manifests
for partOf, group in data_frame.groupby(data_frame['partOf'].fillna(data_frame['img'])):
    group_key = partOf.split('/')[-1]
    # Extract the identifier from the "partOf" URL
    parsed_url = urlparse(group_key)
    extracted_id = parsed_url.path.strip('/').split('/')[-1]
    manifest_id = f"{manifest_server}{project}/{extracted_id}"
    manifest_url = manifest_id+".json"

    # Determine the label for the manifest
    manifest_label = group['partOfTitleStr'].iloc[0] if not pd.isna(group['partOfTitleStr'].iloc[0]) and group['partOfTitleStr'].iloc[0].strip() else group['stillImageUUID'].iloc[0]

    # Create a new manifest with the label
    manifest = Manifest(id=manifest_url, label={"en": [manifest_label]})

    # Set common properties
    manifest.viewingDirection = "left-to-right"
    manifest.requiredStatement = KeyValueString(label="Attribution", value="Provided by DaSCH")
    manifest.summary = ("A IIIF Resource from the BEOL project provided by DaSCH, Swiss National Data and Service Center for the Humanities.")
    # manifest.rights = "http://creativecommons.org/publicdomain/mark/1.0/"

    # Add descriptive metadata to the manifest
    metadata_items = []
    metadata_items.append(KeyValueString(label="Title", value={"en": [group['partOfTitleStr'].iloc[0]]}))
    if 'J' in group.columns and not pd.isna(group['J'].iloc[0]):
        metadata_items.append(KeyValueString(label="Author", value={"en": [group['J'].iloc[0]]}))
    if 'I' in group.columns and not pd.isna(group['I'].iloc[0]):
        metadata_items.append(KeyValueString(label="Recipient", value={"en": [group['I'].iloc[0]]}))
    if 'K' in group.columns and not pd.isna(group['K'].iloc[0]):
        metadata_items.append(KeyValueString(label="System number", value={"en": [group['K'].iloc[0]]}))

    # Check if metadata_items is not empty before setting manifest metadata
    if metadata_items:
        manifest.metadata = metadata_items

    # Set logo and provider
    logo = ResourceItem(id=dasch_logo+"/full/max/0/default.jpg", type="Image", format="image/jpg", height=209, width=557)
    logo.make_service(id=dasch_logo, type="ImageService3", profile="level2")
    provider = ProviderItem(id=dasch_ror, label="DaSCH, Swiss National Data and Service Center for the Humanities", homepage=[HomepageItem(id=dasch_www, type="Text", format="text/html", label="DaSCH, Swiss National Data and Service Center for the Humanities")], logo=[logo])
    manifest.provider = [provider]

    # Create an empty list to store canvases
    canvas_list = []

# Iterate through each row in the group to create canvases
    for _, row in group.sort_values(by="seqnumStr").iterrows():
        canvas_label = row['label']
        still_image_id = row['stillImageUUID']

        # Constructing IDs for canvas, annotation, and annotation page
        canvas_id = f"p{still_image_id}"  # Use stillImageUUID in the canvas ID
        full_canvas_id = f"{manifest_id}/canvas/{canvas_id}"
        anno_id = f"{full_canvas_id}/annotation/{canvas_id}/image"
        anno_page_id = f"{full_canvas_id}/page/{canvas_id}/1"

        # Create and add the canvas using the old script logic
        canvas = manifest.make_canvas_from_iiif(url=f"{sipi_url}{project}/{row['stillImageInternalFilename']}",
                                            label=canvas_label,
                                            id=full_canvas_id,
                                            anno_id=anno_id,
                                            anno_page_id=anno_page_id)
        canvas_list.append(canvas)

        # Create the thumbnail for the manifest (first canvas)
        if canvas_index == 0:
            thumbnail = ResourceItem(id=f"{sipi_url}{project}/{row['stillImageInternalFilename']}/full/80,/0/default.jpg",
                                    type="Image",
                                    format="image/jpeg")
            thumbnail.make_service(id=f"{sipi_url}{project}/{row['stillImageInternalFilename']}",
                                    type="ImageService3",
                                    profile="level2")

    # Add the canvas list to manifest items
    manifest.items = canvas_list

    # Set the thumbnail for the manifest
    if thumbnail:
        manifest.thumbnail = [thumbnail]

    # Extract a valid filename from the manifest_id URL
    filename = os.path.basename(manifest_id)
    # Save the manifest as a JSON file in the 'manifests' directory
    with open(os.path.join(output_dir, f'{filename}.json'), 'w') as json_file:
        json_file.write(manifest.json(indent=2))  # Write the JSON data with indentation