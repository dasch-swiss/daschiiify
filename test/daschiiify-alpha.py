from iiif_prezi3 import Manifest, KeyValueString, ResourceItem, ProviderItem, ExternalItem, HomepageItem
from datetime import datetime, timezone
# import requests (for the DSP API)

# A generic DasCH IIIF Manifest? 
# Like standoff --> mapping for descriptive metadata / which types of resources are relevant?
# 1) Single image 2) Compound object (through Gravsearch our friend)

# The library documentation for generating IIIF resources that are compatible with the Presentation API 3.0 is accessible at https://iiif-prezi.github.io/iiif-prezi3/
# IIIF Template: https://raw.githubusercontent.com/dasch-swiss/iiif-templates/main/boilerplates/boilerplate02.json 
# ARK: https://ark.dasch.swiss/ark:/72163/1/0801/SRj_ydfRQTqkQnWnwHlodw4
# IRI: http://rdfh.ch/0801/SRj_ydfRQTqkQnWnwHlodw 
# DSP API Full Representation: https://api.dasch.swiss/v2/resources/http%3A%2F%2Frdfh.ch%2F0801%2FSRj_ydfRQTqkQnWnwHlodw
# Compare with the experimental IIIF Manifest (https://api.dasch.swiss/v2/resources/iiifmanifest/http%3A%2F%2Frdfh.ch%2F0801%2FSRj_ydfRQTqkQnWnwHlodw)

### IIIF Resource Servers
sipi = "https://iiif.dasch.swiss/"
manifestserver = "https://daschiiify.dasch.swiss/"

### Project and UUID - To be modified and queried from DSP
project = "0801"
dspid = "42"
ark = "https://ark.dasch.swiss/ark:/72163/1/0801/SRj_ydfRQTqkQnWnwHlodw4"

### DSP and DaSCH Website
api = "https://api.dasch.swiss/v2/"
daschlogo = "https://static.wixstatic.com/media/b4d1f5_94a95cd2eab74c2289cbe1bed4fd0dc2~mv2.png"
daschwww = "https://www.dasch.swiss/"
rorid = "https://ror.org/047f01g80"

### Creation of the Manifest
manifest = Manifest(id=manifestserver+dspid+"/manifest.json",
                    label={"en": ["1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I"]})

### Summary of the Resource
manifest.summary = {"en": ["A very nice IIIF Resource provided by DaSCH"],
                    "de": ["Etwas auf Deutsch"]}

### Homepage of the Resource
hitem = HomepageItem(id=ark,type="Text",format="text/html",label={"en": ["Homepage for 1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I"]},language=["en"])
manifest.homepage = [hitem]

### Appending descriptive Metadata, maybe a link to the project? / Permission!
manifest.metadata = [
    KeyValueString(label={"en": ["Title"]}, value={"en": ["1706-11-30_Verzaglia_Giuseppe-Bernoulli_Johann_I"]}),
    KeyValueString(label={"en": ["Recipient"]}, value={"en": ["Johann I Bernoulli"]}),
    KeyValueString(label={"en": ["Author"]}, value={"en": ["Giuseppe Verzaglia"]}),
    KeyValueString(label={"en": ["Date of creation"]}, value={"en": ["GREGORIAN:1706-11-30 CE"]}),
    KeyValueString(label={"en": ["Text"]}, value={"en": ["(...)"]}),
    KeyValueString(label={"en": ["System number"]}, value={"en": ["000057769"]}),
    KeyValueString(label={"en": ["Comment"]}, value={"en": ["Bologna"]}),
    KeyValueString(label={"en": ["Mentioned person"]}, value={"en": ["Jakob I Bernoulli, Ismael Boulliau, John Craig, Jacob Hermann, Gottfried Wilhelm Leibniz, Vittorio Francesco Stancari, John Walli"]}),
]   

### Appending provider, pointing to the Registry of Organizations (ROR), the DaSCH website and its logo (yet, not available via IIIF)
l = ResourceItem(id=daschlogo,type="Image",format="image/png",height=110,width=382)
hdasch = HomepageItem(id=daschwww,type="Text",format="text/html",label={"en": ["DaSCH – Swiss National Data and Service Center for the Humanities"]})
p = ProviderItem(id=rorid, label={"en": ["DaSCH – Swiss National Data and Service Center for the Humanities"]},homepage=[hdasch],logo=[l])
manifest.provider = [p]

### Appending a "seeAlso" property pointing the the DSP API
s = ExternalItem(id=api+"resources/http%3A%2F%2Frdfh.ch%2F0801%2FSRj_ydfRQTqkQnWnwHlodw", format="application/ld+json", type="Dataset", label={"en": ["DaSCH Service Platform (DSP) API V2"]})
manifest.seeAlso = [s]

### We don't have rights metadata in DSP for this record
manifest.rights = "http://creativecommons.org/publicdomain/mark/1.0/"

### This could be serialised differently, also related to rights metadata
manifest.requiredStatement = KeyValueString(label={"en": ["Attribution"]}, value={"en": ["Provided by DaSCH. Public Domain Mark 1.0 - No Known Copyright"]})

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