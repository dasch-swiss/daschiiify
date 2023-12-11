# daschiiify
The purpose of this repository is to develop a script that can generate [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/) resources for DaSCH - Swiss National Data and Service Center for the Humanities leveraging the [iiif-prezi3 Python library](https://iiif-prezi.github.io/iiif-prezi3/). 

The idea is to upgrade the [experimental and outdated IIIF Manifests feature](https://docs.dasch.swiss/2023.02.02/DSP-API/03-endpoints/api-v2/reading-and-searching-resources/#iiif-manifests).

As a first experiment, IIIF Manifests have been created for the [Bernoulli-Euler Online (BEOL)](https://ark.dasch.swiss/ark:/72163/1/0801) project.

## Usage

This repository includes a Python script (`beol.py`) designed to generate IIIF Presentation API 3.0 resources and a Flask web server (`app.py`) that serves as an interface for specifying the manifest server URL.

### Setting Up

Ensure `beol.csv` is placed in the specified location in `app.py`. This CSV file contains the necessary data for generating IIIF resources.

### Running the Flask Server

1. **Start the Server**: Run `app.py` using Python. Ensure Flask is installed in your environment.
   ```bash
   python app.py
   ```
2. **Access the Server**: Open a web browser and navigate to `http://localhost:5000`. This will display a simple user interface.

### Using the Web Interface

1. **Enter the Manifest Server URL**: Use the form to input the URL of the manifest server. This URL is used by `beol.py` to generate the IIIF manifests.
2. **Generate Resources**: Click the 'Generate' button to start the resource generation process. The script will use the provided `manifest_server` URL and the data from `beol.csv` to create IIIF manifests.

### Output

The generated IIIF manifests will be stored in the output directory specified in `beol.py`. The Flask server currently provides a confirmation response after processing. Future updates may include additional functionalities or output handling options.