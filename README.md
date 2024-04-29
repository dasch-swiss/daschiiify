# daschiiify
The purpose of this repository is to develop a script that can generate [IIIF Presentation API 3.0](https://iiif.io/api/presentation/3.0/) resources for DaSCH - Swiss National Data and Service Center for the Humanities leveraging the [iiif-prezi3 Python library](https://iiif-prezi.github.io/iiif-prezi3/). 

This tool aims to upgrade the [experimental and outdated IIIF Manifests feature](https://docs.dasch.swiss/2023.02.02/DSP-API/03-endpoints/api-v2/reading-and-searching-resources/#iiif-manifests) previously available.

As a first experiment, IIIF Manifests have been created for the [Bernoulli-Euler Online (BEOL)](https://ark.dasch.swiss/ark:/72163/1/0801) project.

## Usage

This repository includes a Python script and a Flask web server that serves as an interface for specifying the manifest server URL.

### Setting Up

1. **Prepare the Environment**: Clone the repository and navigate to the project directory.
   ```bash
   git clone https://github.com/dasch-swiss/daschiiify.git
   cd daschiiify
   ```

2. **Install Dependencies**: Make sure Python and Docker are installed on your system. Build the Docker image using the provided Dockerfile.
   ```bash
   docker build -t daschiiify .
   ```

3. **Prepare SSL Certificates**: The server uses HTTPS, so you'll need to generate a private key and a self-signed certificate. Store these in the `certs` directory.
   ```bash
   mkdir -p certs
   openssl genrsa -out certs/key.pem 2048
   openssl req -new -key certs/key.pem -out certs/cert.csr
   openssl req -x509 -days 365 -key certs/key.pem -in certs/cert.csr -out certs/cert.pem
   ```

### Running the Flask Server

1. **Run the Docker Container**: Start the container which runs the Flask server.
   ```bash
   docker run -p 5000:5000 daschiiify
   ```

2. **Access the Server**: Open a web browser and navigate to [https://127.0.0.1:5000](https://127.0.0.1:5000). This will display the user interface.

### Using the Web Interface

- **Enter the Manifest Server URL**: Input the URL of the manifest server in the form provided. This URL is used by the script to generate IIIF manifests.
- **Generate Resources**: Click the 'Generate IIIF Resources' button to start the resource generation process using the specified `manifest_server` URL and data from `beol.csv`.
- **Amend JSON Files**: Click 'Amend JSON Files by setting the correct HTTPS URL from SIPI' to adjust the URLs in the generated JSON files from HTTP to HTTPS, preventing mixed content issues.

### Docker Image Build Process

The Dockerfile provided in this repository uses a multi-stage build process to optimize the size of the final Docker image. It separates the build environment from the production environment, resulting in a smaller image size.

- build_release: This stage sets up the build environment, installs dependencies, and prepares the application for production.
- build_dev: In this stage, additional files specific to development, such as data directories, are added to the image.
- Final Image Selection: The final image is selected based on the value of the `BUILD_ENV` argument provided during the build process. If `BUILD_ENV=release`, the build_release stage is used; otherwise, the `build_dev` stage is selected.

### Output

The generated IIIF manifests are stored in the `data/0801` directory within the container, accessible through the Flask server. Future updates may include additional functionalities or output handling options.

_For the moment, only IIIF Manifests for the BEOL project can be generated, but it is intended that the script will be amended to accomodate different projects hosted on the DaSCH Service Platform_
