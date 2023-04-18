import os
import glob
from flask import Flask, render_template, request, send_file, redirect

app = Flask(__name__)

# Path to the directory containing the files
UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'upload'))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Get a list of all the files in the directory
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    # Render the template with the list of files
    return render_template('index.html', files=files)

@app.route('/download/<filename>')
def download(filename):
    # Path to the file to be downloaded
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # Return the file as an attachment
    return send_file(filepath, as_attachment=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded files
        uploaded_files = request.files.getlist('file[]')
        # Save each file to the server
        for file in uploaded_files:
            if file.filename:
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            else:
                return redirect('/')
        # Redirect to the homepage to show the updated file list
        os.mknod(os.path.join(app.config['UPLOAD_FOLDER'], 'sign.txt'))
        return redirect('/')
    # Render the upload form
    return render_template('upload.html')

@app.route('/delete/<filename>', methods=['POST'])
def delete(filename):
    # Construct the full path to the file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # Delete the file
    os.remove(filepath)
    # Redirect back to the index page
    return redirect('/')

@app.route('/deleteall', methods=['POST'])
def deleteall():
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], '*')
    files = glob.glob(filepath)
    for f in files:
        os.remove(f)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8018, debug = True)

