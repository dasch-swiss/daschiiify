# daschiiify
The purpose of this repository is to develop a script that can generate [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/) resources for DaSCH - Swiss National Data and Service Center for the Humanities leveraging the [iiif-prezi3 Python library](https://iiif-prezi.github.io/iiif-prezi3/). 

The idea is to upgrade the [experimental and outdated IIIF Manifests feature](https://docs.dasch.swiss/2023.02.02/DSP-API/03-endpoints/api-v2/reading-and-searching-resources/#iiif-manifests).

As a first experiment, IIIF Manifests have been created for the [Bernoulli-Euler Online (BEOL)](https://ark.dasch.swiss/ark:/72163/1/0801) project.

## Usage

This repository includes a Flask web server (`app.py`) and a Python script (`beol.py`) designed to generate IIIF Presentation API 3.0 resources.

### Running the Flask Server

1. **Start the Server**: Run `app.py` using Python. Make sure Flask is installed in your environment.
   ```bash
   python app.py
   ```
2. **Access the Server**: Open a web browser and go to `http://localhost:5000`. This will bring up a user interface for uploading a CSV file.

### Using the Web Interface

1. **Upload a CSV File**: Use the provided form to upload a CSV file. This file should contain the necessary data for generating IIIF resources.
2. **Specify the Manifest Server URL**: Enter the URL of the manifest server in the provided field. This URL is used by `beol.py` to generate the IIIF manifests.
3. **Submit**: After uploading the CSV file and entering the manifest server URL, click the 'Upload' button to process the file.

### Script Execution

Upon submission, the Flask server will:
- Save the uploaded CSV file.
- Run `beol.py`, passing the CSV file path and the manifest server URL as arguments.
- Generate IIIF manifests based on the provided data.

### Output

The generated IIIF manifests are stored in a specified output directory. The Flask server currently provides a placeholder response after processing. Future updates may include direct links to the generated manifests or display options within the web interface.