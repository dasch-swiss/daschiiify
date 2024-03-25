# daschiiify
The purpose of this repository is to develop a script that can generate [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/) resources for DaSCH - Swiss National Data and Service Center for the Humanities leveraging the [iiif-prezi3 Python library](https://iiif-prezi.github.io/iiif-prezi3/). 

The idea is to upgrade the [experimental and outdated IIIF Manifests feature](https://docs.dasch.swiss/2023.02.02/DSP-API/03-endpoints/api-v2/reading-and-searching-resources/#iiif-manifests).

As a first experiment, IIIF Manifests have been created for the [Bernoulli-Euler Online (BEOL)](https://ark.dasch.swiss/ark:/72163/1/0801) project.

## Usage

This repository includes a Python script (`beol-iiif.py`) designed to generate IIIF Presentation API 3.0 resources and a Flask web server (`app.py`) that serves as an interface for specifying the manifest server URL.

### Setting Up

Ensure `beol.csv` is placed in the specified location in `app.py`. This CSV file contains the necessary data for generating IIIF resources.

### Running the Flask Server

1. **Generate a private key and a Self-Signed Certificate** Those files must remain hidden.
   
   Private key (`key.pem`)
   ```bash
   openssl genrsa -out key.pem 2048
   ```
   This command generates a private key (key.pem) with a length of 2048 bits.

   Create a Certificate Signing Request (CSR) using the private key generated in the previous step. Execute the following command (`cert.csr`):

   ```bash
   openssl req -new -key key.pem -out cert.csr
   ```

   Generate a self-signed certificate (`cert.pem`)
   ```bash
   openssl req -x509 -days 365 -key key.pem -in cert.csr -out cert.pem
   ```
   This command will create a self-signed certificate valid for 365 days.

2. **Start the Server**: Run `app.py` using Python. Ensure Flask is installed in your environment.
   ```bash
   python app.py
   ```
2. **Access the Server**: Open a web browser and navigate to [https://127.0.0.1:5000](https://127.0.0.1:5000). This will display a simple user interface.

### Using the Web Interface

1. **Enter the Manifest Server URL**: Use the form to input the URL of the manifest server. This URL is used by `beol-iiif.py` to generate the IIIF manifests.
2. **Generate Resources**: Click the 'Generate IIIF Resources' button to start the resource generation process. The script will use the provided `manifest_server` URL and the data from `beol.csv` to create IIIF manifests.
3. **Amend the JSON files**: In our current setup, the `beol-iiif.py` script designed to retrieve URLs from the DaSCH SIPI instance – a server compliant with the IIIF Image API – defaults to fetching URLs using the HTTP protocol. This behaviour can lead to mixed content issues when these URLs are used in a context that requires HTTPS. To address this, there is a workaround that involves running a Python script to convert these URLs from HTTP to HTTPS. By clicking on 'Amend JSON Files by setting the correct HTTPS URL from SIPI', the URLs are corrected by leveraging the `replace-sipi-url.py` script. 

### Output

The generated IIIF manifests will be stored in the output directory specified in `beol-iiif.py`. The Flask server currently provides a confirmation response after processing. Future updates may include additional functionalities or output handling options.