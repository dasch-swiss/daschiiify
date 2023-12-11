from flask import Flask, request, render_template_string
import subprocess
import os

# Flask app setup
app = Flask(__name__)
csv_file_path = 'path/to/beol.csv'  # Update this path to where beol.csv is stored

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        manifest_server = request.form['manifest_server']
        # Run the script with the beol.csv file and the manifest server URL
        script_command = f'python beol.py --csv {csv_file_path} --manifest_server {manifest_server}'
        subprocess.run(script_command, shell=True)
        return 'IIIF resources generated successfully.'
    
    return render_template_string('''
        <!doctype html>
        <title>Set Manifest Server</title>
        <h1>Enter Manifest Server URL</h1>
        <form method="post">
            <input type="text" name="manifest_server" placeholder="Enter manifest server URL">
            <input type="submit" value="Generate">
        </form>
    ''')

if __name__ == '__main__':
    app.run(debug=True)