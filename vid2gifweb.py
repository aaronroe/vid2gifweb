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
	print file
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		name_with_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(name_with_path)
		
		VideoFileClip(name_with_path).subclip((0,1.0),(0,2.0)).resize(0.3).to_gif("converted/"+filename.rsplit('.', 1)[0]+".gif")

		os.remove(name_with_path)

	return ""

if __name__ == "__main__":
    app.run(debug=True)