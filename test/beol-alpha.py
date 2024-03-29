from iiif_prezi3 import config, Manifest, KeyValueString, ResourceItem, ProviderItem, ExternalItem, HomepageItem
from datetime import datetime, timezone

# A generic DasCH IIIF Manifest? 
# Like standoff --> mapping for descriptive metadata / which types of resources are relevant?
# 1) Single image 2) Compound object (through Gravsearch)

# The library documentation for generating IIIF resources that are compatible with the Presentation API 3.0 is accessible at https://iiif-prezi.github.io/iiif-prezi3/
# IIIF Template: https://raw.githubusercontent.com/dasch-swiss/iiif-templates/main/boilerplates/boilerplate02.json 
# ARK: https://ark.dasch.swiss/ark:/72163/1/0801/SRj_ydfRQTqkQnWnwHlodw4
# IRI: http://rdfh.ch/0801/SRj_ydfRQTqkQnWnwHlodw 
# DSP API Full Representation: https://api.dasch.swiss/v2/resources/http%3A%2F%2Frdfh.ch%2F0801%2FSRj_ydfRQTqkQnWnwHlodw
# Compare with the experimental IIIF Manifest (https://api.dasch.swiss/v2/resources/iiifmanifest/http%3A%2F%2Frdfh.ch%2F0801%2FSRj_ydfRQTqkQnWnwHlodw)

### IIIF Resource Servers
sipi = "https://iiif.dasch.swiss/"
manifestserver = "https://iiif-manifest.dasch.swiss/"

### Project and UUID - To be modified and queried from DSP
project = "0801"
dspid = "42"
ark = "https://ark.dasch.swiss/ark:/72163/1/0801/SRj_ydfRQTqkQnWnwHlodw4"

### DSP and DaSCH Website
api = "https://api.dasch.swiss/v2/"
daschlogo = "https://iiif.dasch.swiss/0810/7WumAIYuJsQ-CroJQljo3CV.jp2/full/max/0/default.jpg"
daschwww = "https://www.dasch.swiss/"
rorid = "https://ror.org/047f01g80"

### Language maps only in English
config.configs['helpers.auto_fields.AutoLang'].auto_lang = "en"

### Creation of the Manifest
manifest = Manifest(id=manifestserver+dspid+"/manifest.json",
                    label="1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I")

### Summary of the Resource
manifest.summary = ("A very nice IIIF Resource provided by DaSCH")

### Homepage of the Resource
hitem = HomepageItem(id=ark,type="Text",format="text/html",label="Homepage for 1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I")
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
l = ResourceItem(id=daschlogo,type="Image",format="image/jpg",height=209,width=557)
l.make_service(id="https://iiif.dasch.swiss/0810/7WumAIYuJsQ-CroJQljo3CV.jp2",
                    type="ImageService3",
                    profile="level2")
hdasch = HomepageItem(id=daschwww,type="Text",format="text/html",label="DaSCH, Swiss National Data and Service Center for the Humanities")
p = ProviderItem(id=rorid, label="DaSCH, Swiss National Data and Service Center for the Humanities",homepage=[hdasch],logo=[l])
manifest.provider = [p]

### Appending a "seeAlso" property pointing the the DSP API
s = ExternalItem(id=api+"resources/http%3A%2F%2Frdfh.ch%2F0801%2FSRj_ydfRQTqkQnWnwHlodw", format="application/ld+json", type="Dataset", label="DaSCH Service Platform (DSP) API V2")
manifest.seeAlso = [s]

### We don't have rights metadata in DSP for this record
manifest.rights = "http://creativecommons.org/publicdomain/mark/1.0/"

### This could be serialised differently, also related to rights metadata
manifest.requiredStatement = KeyValueString(label="Attribution", value="Provided by DaSCH. Public Domain Mark 1.0 - No Known Copyright")

### We don't have such metadata but by default, we could assume that is left-to-right
manifest.viewingDirection = "left-to-right"

manifest.navDate = datetime(1706, 11, 30, tzinfo=timezone.utc)

### Thumbnail

thumbnail = ResourceItem(id=sipi+project+"/4VjgCwiTn8p-CTaooIqSZBO.jpx/full/80,/0/default.jpg",
                         type="Image",
                         format="image/jpeg")

thumbnail.make_service(id=sipi+project+"/4VjgCwiTn8p-CTaooIqSZBO.jpx",
                       type="ImageService3",
                       profile="level2")

manifest.thumbnail = [thumbnail]


### Canvases - how to find the correct IIIF Image API URLs through DSP?

# Resource > Representation > File ? 
# IIIF Image API Info JSON: knora-api:fileValueAsUrl (but up to id.filename) + Canvas Label: knora-api:fileValueHasFilename	

canvas1 = manifest.make_canvas_from_iiif(url=sipi+project+"/4VjgCwiTn8p-CTaooIqSZBO.jpx",
                                        label="1383232",
                                        id=manifestserver + dspid + "/canvas/p1",
                                        anno_id=manifestserver + dspid + "/annotation/p0001-image",
                                        anno_page_id=manifestserver + dspid + "/page/p1/1")

canvas2 = manifest.make_canvas_from_iiif(url=sipi+project+"/DxeENcvqYzJ-GPOelprhbJU.jpx",
                                        label="1383234",
                                        id=manifestserver + dspid + "/canvas/p2",
                                        anno_id=manifestserver + dspid + "/annotation/p0002-image",
                                        anno_page_id=manifestserver + dspid + "/page/p2/1")

canvas3 = manifest.make_canvas_from_iiif(url=sipi+project+"/7OdK2SkmyXf-GMzUkg1GYkU.jpx",
                                        label="1383235",
                                        id=manifestserver + dspid + "/canvas/p3",
                                        anno_id=manifestserver + dspid + "/annotation/p0003-image",
                                        anno_page_id=manifestserver + dspid + "/page/p3/1")

canvas4 = manifest.make_canvas_from_iiif(url=sipi+project+"/9dHDpkvAV8C-EbHjcdgyifD.jpx",
                                        label="1383236",
                                        id=manifestserver + dspid + "/canvas/p4",
                                        anno_id=manifestserver + dspid + "/annotation/p0004-image",
                                        anno_page_id=manifestserver + dspid + "/page/p4/1")

print(manifest.json(indent=2))