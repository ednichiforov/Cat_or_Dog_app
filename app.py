from flask import Flask, render_template, request, redirect, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES
from model import make_prediction
from pathlib import Path
import os
import shutil

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

configure_uploads(app, photos)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        if 'file' not in request.files:
            flash("No file chosen")
            return redirect(request.url)
        else:
            filename = photos.save(request.files['photo'])
            filename_path = os.path.join(Path('uploads'), filename)
            cat_or_dog = make_prediction(filename_path)
            try:
                shutil.rmtree('uploads')
            except OSError as e:
                return "Error: %s - %s." % (e.filename, e.strerror)
            return "It's a {}".format(cat_or_dog)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
