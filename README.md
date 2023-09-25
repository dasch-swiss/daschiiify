# daschiiify
The purpose of this repository is to develop a script that can generate [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/) resources for DaSCH - Swiss National Data and Service Center for the Humanities leveraging the [iiif-prezi3 Python library](https://iiif-prezi.github.io/iiif-prezi3/). 

The idea is to use the DaSCH Service Platform (DSP) API and the IIIF Image API 3.0 — through our Simple Image Presentation Interface (SIPI) instance — for populating the IIIF resources (`Manifest` and `Collection`) and to upgrade the [experimental and outdated IIIF Manifests feature](https://docs.dasch.swiss/2023.02.02/DSP-API/03-endpoints/api-v2/reading-and-searching-resources/#iiif-manifests).

![High-level overview](overview.png)

At the moment, an [alpha script](/test/daschiiify-alpha.py) is in development to generate a particular IIIF resource, still waiting on how to leverage the DSP API in an efficient manner. 

## Requirements
- [ ] Populating the Presentation API resources through DSP API requests, possibly without reyling too much on Gravsearch, a Virtual Graph Search (cf. https://doi.org/10.3233/SW-200386)
- [ ] Finding the correct IIIF Image API URLs to build the series of `Canvas`
- [ ] IIIF Manifests and Collections should have their own subdomain (e.g. `https://manifests.dasch.swiss/`) and they should not be stored where the DSP API lives
- [x] The DaSCH logo should ideally be served through our SIPI instance

## Open questions
- How to find easily which records (image-based, sound, video) can be genereated into IIIF resources?
- What kind of assumptions should be done when we don't have the metadata (e.g. assuming `left-to-right` structural sequence for multi-page Manifests or rights metadata)?
- Which descriptive metadata should be appended to the `metadata` property in our IIIF resources (all of them, a selection)?
- Do we want to provide titles (`label`), descriptions (`summary`) and descriptive metadata (`metadata`) in multiple languages (cf. [Internationalization and Multi-language Values](https://iiif.io/api/cookbook/recipe/0006-text-language/))? For the moment, it is done only in English. 
- How should the `daschiiify` script be leveraged within the DaSCH infrastructure once it's stable?

## Templates
The templates or boilerplates have been documented and stored on this [dedicated repository](https://github.com/dasch-swiss/iiif-templates). 