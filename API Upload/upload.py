import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './Archivos'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def upload_file():
    return render_template('formulario.html')


@app.route("/upload", methods=['GET','POST'])
def uploader():
    if request.method == 'POST':
        file = request.files['archivo']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return "<h1>Archivo subido exitosamente</h1>"


if __name__ == '__main__':
    app.run(host="localhost", port=6060, debug=True)
