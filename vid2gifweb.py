import os
from flask import Flask, request
from werkzeug.utils import secure_filename
from moviepy.editor import *
from flask.ext.pymongo import PyMongo

UPLOAD_FOLDER = 'file-uploads'
ALLOWED_EXTENSIONS = set(['mp4'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

mongo = PyMongo(app)

def allowed_file(filename):
  return '.' in filename and \
		filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/uploads")
def view_uploads():
	rows = ""
	for i in range(mongo.db.fs.files.find().count()):
		rows += str(mongo.db.fs.files.find()[i])
	return rows

@app.route("/upload", methods=['POST'])
def upload_video():
	file = request.files['video']
	
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		name_with_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
		file.save(name_with_path)
		
		gifname = filename.rsplit('.', 1)[0]+".gif"
		gifpath = "converted/"+gifname

		# create the 0-5 second gif at 0.3 of the size
		VideoFileClip(name_with_path).subclip((0,0.0),(0,5.0)).resize(0.3).to_gif("converted/"+gifname)
		
		# save the converted gif to mongofs
		giffile = open(gifpath)
		mongo.save_file(gifname, giffile)
		giffile.close()

		# remove temporarily stored files
		os.remove(name_with_path)
		os.remove(gifpath)

		print mongo.db.fs.files.find().count()

	return ""

if __name__ == "__main__":
    app.run(debug=True)