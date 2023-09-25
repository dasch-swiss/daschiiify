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
dasch_logo = "https://iiif.dasch.swiss/0810/7WumAIYuJsQ-CroJQljo3CV.jp2/full/max/0/default.jpg"
dasch_www = "https://www.dasch.swiss/"
dasch_ror = "https://ror.org/047f01g80"

### IDs
project = "0801"
internal_link = ""
internal_id = ""
ark_id = "" - # see https://github.com/dasch-swiss/ark-resolver/blob/master/src/base64url_check_digit.py
dsp_id = "" # to be found

### Language maps only in English
config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

### Creation of the Manifest
manifest = Manifest(id=manifest_server+project+dsp_id+"/manifest.json",
                    label="1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I")

### Summary of the Resource
manifest.summary = ("A IIIF Resource provided by DaSCH")

### Homepage of the Resource
hitem = HomepageItem(id=ark_id,type="Text",format="text/html",label="Homepage for 1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I")
manifest.homepage = [hitem]

### Appending descriptive Metadata, maybe a link to the project? / Permission!
manifest.metadata = [
    KeyValueString(label="Title", value="1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I"),
    KeyValueString(label="Recipient", value="Johann I Bernoulli"),
    KeyValueString(label="Author", value="Giuseppe Verzaglia"),
    KeyValueString(label="Date of creation", value="GREGORIAN:1706-11-30 CE"),
    KeyValueString(label="System number", value="000057769"),
    KeyValueString(label="Comment", value="Bologna"),
    KeyValueString(label="Mentioned person", value="Jakob I Bernoulli, Ismael Boulliau, John Craig, Jacob Hermann, Gottfried Wilhelm Leibniz, Vittorio Francesco Stancari, John Walli"),
]   

### Appending provider, pointing to the Registry of Organizations (ROR), the DaSCH website and its logo
l = ResourceItem(id=dasch_logo,type="Image",format="image/jpg",height=209,width=557)
l.make_service(id="https://iiif.dasch.swiss/0810/7WumAIYuJsQ-CroJQljo3CV.jp2",
                    type="ImageService3",
                    profile="level2")
hdasch = HomepageItem(id=dasch_www,type="Text",format="text/html",label="DaSCH, Swiss National Data and Service Center for the Humanities")
p = ProviderItem(id=dasch_ror, label="DaSCH, Swiss National Data and Service Center for the Humanities",homepage=[hdasch],logo=[l])
manifest.provider = [p]

### Appending a "seeAlso" property pointing the the DSP API
# s = ExternalItem(id=dsp_api+ark_id, format="application/ld+json", type="Dataset", label="DaSCH Service Platform (DSP) API V2")
# manifest.seeAlso = [s]

### Rights 
# manifest.rights = "http://creativecommons.org/publicdomain/mark/1.0/"

### Required Statement
manifest.requiredStatement = KeyValueString(label="Attribution", value="Provided by DaSCH.")

### We don't have such metadata but by default, we could assume that is left-to-right
manifest.viewingDirection = "left-to-right"

# navDate
# manifest.navDate = datetime(YYYY, MM, DD, tzinfo=timezone.utc)

### Thumbnail

thumbnail = ResourceItem(id=sipi+project+stillImageInternalFilename+"/full/80,/0/default.jpg",
                         type="Image",
                         format="image/jpeg")

thumbnail.make_service(id=sipi+project+stillImageInternalFilename,
                       type="ImageService3",
                       profile="level2")

manifest.thumbnail = [thumbnail]


### Canvases

canvas1 = manifest.make_canvas_from_iiif(url=sipi+project+"/4VjgCwiTn8p-CTaooIqSZBO.jpx",
                                        label="1383232",
                                        id=manifest_server + dsp_id + "/canvas/p1",
                                        anno_id=manifest_server + dsp_id + "/annotation/p0001-image",
                                        anno_page_id=manifest_server + dsp_id + "/page/p1/1")

canvas2 = manifest.make_canvas_from_iiif(url=sipi+project+"/DxeENcvqYzJ-GPOelprhbJU.jpx",
                                        label="1383234",
                                        id=manifest_server + dsp_id + "/canvas/p2",
                                        anno_id=manifest_server + dsp_id + "/annotation/p0002-image",
                                        anno_page_id=manifest_server + dsp_id + "/page/p2/1")

canvas3 = manifest.make_canvas_from_iiif(url=sipi+project+"/7OdK2SkmyXf-GMzUkg1GYkU.jpx",
                                        label="1383235",
                                        id=manifest_server + dsp_id + "/canvas/p3",
                                        anno_id=manifest_server + dsp_id + "/annotation/p0003-image",
                                        anno_page_id=manifest_server + dsp_id + "/page/p3/1")

canvas4 = manifest.make_canvas_from_iiif(url=sipi+project+"/9dHDpkvAV8C-EbHjcdgyifD.jpx",
                                        label="1383236",
                                        id=manifest_server + dsp_id + "/canvas/p4",
                                        anno_id=manifest_server + dsp_id + "/annotation/p0004-image",
                                        anno_page_id=manifest_server + dsp_id + "/page/p4/1")

print(manifest.json(indent=2))