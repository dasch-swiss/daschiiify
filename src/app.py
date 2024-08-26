#!/usr/bin/env python
from flask import Flask, request, render_template_string, send_from_directory, redirect, url_for
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

# Set relative paths for the data
project = '0801'
base_dir = os.path.dirname(__file__)
csv_file_path = os.path.join(base_dir, '..', 'data', 'beol.csv')  # Relative path to CSV
data_folder = os.path.join(base_dir, '..', 'data', project)  # Relative path to project-specific data directory
file_generation_enabled = True

# Ensure 'data/0801' directory exists
if not os.path.exists(data_folder):
    os.makedirs(data_folder, exist_ok=True)  # Using exist_ok=True to avoid FileExistsError

@app.route('/', methods=['GET', 'POST'])
def index():
    log_output = ""
    file_list = os.listdir(data_folder)  # List files in the data directory

    if request.method == 'POST' and file_generation_enabled:
        manifest_server = request.form['manifest_server']
        script_command = f'python {os.path.join(base_dir, "beol-iiif.py")} --csv "{csv_file_path}" --manifest_server "{manifest_server}"'
        
        # Execute the script and capture output
        result = subprocess.run(script_command, shell=True, capture_output=True, text=True)
        
        # Capture the output and errors
        log_output = f"Output:\n{result.stdout}\nError:\n{result.stderr}"
        file_list = os.listdir(data_folder)  # Update file list after script execution

    return render_template_string('''
        <!doctype html>
        <title>Generate IIIF Resources</title>
        <h1>Enter Manifest Server URL and Generate IIIF Resources</h1>
        <form method="post">
            <input type="text" name="manifest_server" placeholder="Enter manifest server URL">
            <input type="submit" value="Generate">
        </form>
        <form method="post" action="{{ url_for('toggle_generation') }}">
            <input type="submit" value="Toggle File Generation">
        </form>
        <form method="post" action="{{ url_for('amend_json') }}">
            <input type="submit" value="Amend JSON Files by setting the correct HTTPS URL from SIPI">
        </form>
        <h2>Log Output</h2>
        <pre>{{ log_output }}</pre>
        <h2>Generated Files</h2>
        <ul>
            {% for file in file_list %}
                <li><a href="{{ url_for('serve_data', filename=file) }}">{{ file }}</a></li>
            {% endfor %}
        </ul>
    ''', log_output=log_output, file_list=file_list)

@app.route('/toggle-generation', methods=['POST'])
def toggle_generation():
    global file_generation_enabled
    file_generation_enabled = not file_generation_enabled
    return redirect(url_for('index'))

@app.route('/amend-json', methods=['POST'])
def amend_json():
    script_command = f'python {os.path.join(base_dir, "replace-sipi-url.py")}'
    subprocess.run(script_command, shell=True)
    return redirect(url_for('index'))

@app.route(f'/data/{project}/<path:filename>')
def serve_data(filename):
    if filename.endswith('.DS_Store'):
        return "Access denied", 403  # Block access to .DS_Store files
    return send_from_directory(data_folder, filename)

if __name__ == '__main__':
    ssl_context = (
        os.path.join(base_dir, '..', 'certs', 'cert.pem'),
        os.path.join(base_dir, '..', 'certs', 'key.pem')
    )  # Correct path to SSL certificates
    app.run(debug=True, ssl_context=ssl_context, host='0.0.0.0', port=5000)
