import os
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
        for file in uploaded_files:
            # Save each file to the server
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # Redirect to the homepage to show the updated file list
        return redirect('/')
    # Render the upload form
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug = True)

