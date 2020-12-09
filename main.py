from flask import Flask, flash, request, render_template, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
app = Flask(__name__, static_url_path ='/static')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
lat = 0
longt = 0
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def welcome():
    imageList = os.listdir('static/uploads/')
    imagelist = ['static/uploads/' + image for image in imageList]
    return render_template("listImage.html", imagelist=imagelist)
@app.route('/map')
def hello_world():
    return render_template('hello.html',latitude = lat, longtitude = longt)

@app.route('/upload')
def uploader_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload():
    imageName = request.args.get('name', type=str)
    if 'file' not in request.files:
        flash('No file part')
        return redirect("/upload")
    file = request.files['file']
    if file.filename == '' or imageName == None:
        flash('No image selected for uploading')
        return redirect("/upload")
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
		#print('upload_image filename: ')
        flash('Image successfully uploaded and displayed')
        return render_template('upload.html', filename=filename)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect("/upload")
@app.route('/deleteImage', methods=['GET'])
def delete():
    image = request.args.get('image', default="*", type=str)
    print(image)
    os.remove(image)
    return redirect("/")

if __name__ == '__main__':
    app.run()
