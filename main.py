from flask import Flask, flash, request, render_template, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
app = Flask(__name__, static_url_path ='/static')

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def welcome():
    imageList = os.listdir('static/uploads/')
    imagelist = ['static/uploads/' + image for image in imageList]
    return render_template("listImage.html", imagelist=imagelist)
@app.route('/map')
def hello_world():
    return render_template('hello.html', name="List Image")

@app.route('/upload')
def uploader_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
        # flash('Image successfully uploaded and displayed')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)

if __name__ == '__main__':
    app.run()
