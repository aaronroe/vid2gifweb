import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from moviepy.editor import *

UPLOAD_FOLDER = 'file-uploads'
ALLOWED_EXTENSIONS = set(['mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/upload", methods=['POST'])
def upload_video():
	file = request.files['video']
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print file
	return ""

if __name__ == "__main__":
    app.run(debug=True)