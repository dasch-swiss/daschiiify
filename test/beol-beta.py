import pandas as pd
from iiif_prezi3 import config, Manifest, KeyValueString, ResourceItem, ProviderItem, ExternalItem, HomepageItem
# from datetime import datetime, timezone

### Script to generate BEOL IIIF Manifests based on a CSV which resulted from a SPARQL query.

# Load the CSV data into a DataFrame
csv_file_path = 'beol.csv'
data_frame = pd.read_csv(csv_file_path)

### Servers and DaSCH Links
sipi = "https://iiif.dasch.swiss/"
manifest_server = "https://manifests.dasch.swiss/"
dsp_api = "https://api.dasch.swiss/v2/"
dasch_logo = "https://iiif.dasch.swiss/0810/7WumAIYuJsQ-CroJQljo3CV.jp2"
dasch_www = "https://www.dasch.swiss/"
dasch_ror = "https://ror.org/047f01g80"

### IDs
project = "0801"
internal_link = ""
internal_id = ""
manifest_id = ""
still_image_id = ""
ark_id = "" - # see https://github.com/dasch-swiss/ark-resolver/blob/master/src/base64url_check_digit.py

### Language maps only in English
config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

### Creation of the Manifest
manifest = Manifest(id=manifest_server+"/"+project+"/"+manifest_id+"/manifest.json")

### Label, Summary of the Resource
manifest.label = ("A IIIF Resource provided by DaSCH")
manifest.summary = ("A IIIF Resource provided by DaSCH")

### Homepage of the Resource
hitem = HomepageItem(id=ark_id,type="Text",format="text/html",label="Homepage")
manifest.homepage = [hitem]

### Descriptive Metadata
manifest.metadata = [
    KeyValueString(label="Title", value="1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I"),
    KeyValueString(label="Recipient", value="Johann I Bernoulli"),
    KeyValueString(label="System number", value="000057769"),
]   

### Provider and Logo
l = ResourceItem(id=dasch_logo+"/full/max/0/default.jpg",type="Image",format="image/jpg",height=209,width=557)
l.make_service(id=dasch_logo,
                    type="ImageService3",
                    profile="level2")
hdasch = HomepageItem(id=dasch_www,type="Text",format="text/html",label="DaSCH, Swiss National Data and Service Center for the Humanities")
p = ProviderItem(id=dasch_ror, label="DaSCH, Swiss National Data and Service Center for the Humanities",homepage=[hdasch],logo=[l])
manifest.provider = [p]

### Appending a "seeAlso" property pointing the the DSP API
# s = ExternalItem(id=dsp_api+internal_id, format="application/ld+json", type="Dataset", label="DaSCH Service Platform (DSP) API V2")
# manifest.seeAlso = [s]

### Required Statement and Rights
manifest.requiredStatement = KeyValueString(label="Attribution", value="Provided by DaSCH.")
# manifest.rights = "http://creativecommons.org/publicdomain/mark/1.0/"

### Directionality - we don't have such metadata but by default, we could assume that is left-to-right
manifest.viewingDirection = "left-to-right"

# navDate
# manifest.navDate = datetime(YYYY, MM, DD, tzinfo=timezone.utc)

### Thumbnail

thumbnail = ResourceItem(id=sipi+project+still_image_id+"/full/80,/0/default.jpg",
                         type="Image",
                         format="image/jpeg")

thumbnail.make_service(id=sipi+project+still_image_id,
                       type="ImageService3",
                       profile="level2")

manifest.thumbnail = [thumbnail]


### Canvases
canvas_id = 1
canvas = manifest.make_canvas_from_iiif(url=sipi+project+still_image_id,
                                        label="1383232",
                                        id=manifest_server + manifest_id + "/canvas/"+"p"+canvas_id",
                                        anno_id=manifest_server + manifest_id + "/annotation/p0001-image",
                                        anno_page_id=manifest_server + manifest_id + "/page/p"+canvas_id+"/1")

print(manifest.json(indent=2))