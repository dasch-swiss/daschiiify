# Old README

The [alpha](beol-alpha.py.py) and [beta](beol-beta.py) scripts were created to generate a particular IIIF resource from the BEOL project.

## Requirements
- [ ] Populating the Presentation API resources through DSP API requests, possibly without reyling too much on Gravsearch, a Virtual Graph Search (cf. https://doi.org/10.3233/SW-200386)
- [ ] Finding the correct IIIF Image API URLs to build the series of `Canvas`
- [ ] IIIF Manifests and Collections should have their own subdomain (e.g. `https://iiif-manifest.dasch.swiss/`) and they should not be stored where the DSP API lives
- [x] The DaSCH logo should ideally be served through our SIPI instance

## Open questions
- How to find easily which records (image-based, sound, video) can be genereated into IIIF resources?
- What kind of assumptions should be done when we don't have the metadata (e.g. assuming `left-to-right` structural sequence for multi-page Manifests or rights metadata)?
- Which descriptive metadata should be appended to the `metadata` property in our IIIF resources (all of them, a selection)?
- Do we want to provide titles (`label`), descriptions (`summary`) and descriptive metadata (`metadata`) in multiple languages (cf. [Internationalization and Multi-language Values](https://iiif.io/api/cookbook/recipe/0006-text-language/))? For the moment, it is done only in English. 
- How should the `daschiiify` script be leveraged within the DaSCH infrastructure once it's stable?

## Templates
The templates or boilerplates have been documented and stored on this [dedicated repository](https://github.com/dasch-swiss/iiif-templates). 