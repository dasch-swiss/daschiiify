
from flask import Flask, request, redirect, url_for
import os
import subprocess
import uuid

# Flask app setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['GENERATED_FOLDER'] = 'generated'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB upload limit

# Ensure the upload and generated directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['GENERATED_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        manifest_server = request.form['manifest_server']
        # If the user does not select a file, the browser submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and manifest_server:
            # Save the uploaded file
            filename = str(uuid.uuid4()) + '.csv'
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Run the script with the uploaded CSV file
            output_folder = os.path.join(app.config['GENERATED_FOLDER'], str(uuid.uuid4()))
            os.makedirs(output_folder, exist_ok=True)
            script_command = f'python beol.py --csv {file_path} --manifest_server {manifest_server}'
            subprocess.run(script_command, shell=True)

            # TODO: Provide a way to display or download the generated manifests
            return redirect(url_for('uploaded_file', filename=filename))
    
    return '''
    <!doctype html>
    <title>Upload CSV File</title>
    <h1>Upload a CSV file to generate IIIF resources</h1>
    <form method=post enctype=multipart/form-data>
      <input type=text name=manifest_server placeholder="Enter manifest server URL">
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # TODO: Display or provide links to generated manifests
    return f'File {filename} uploaded and processed.'

# Placeholder for running the app
# app.run(debug=True)
