from .config import config
from PIL import Image
from flask import Flask, request
from . import png2ansi
import os

# example: curl -F "file=@sample.png"  localhost:5000/upload

app = Flask(__name__)
app.config.from_object(config)


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files: return ('Error: No file given')
        
        file = request.files['file']
        absfile = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(absfile)

        # Check fileformat
        with  Image.open(absfile) as img: imgformat = img.format
        if imgformat !='PNG': return ('Error: file must be PNG image')

        ansistr = png2ansi.convert(absfile)
        os.remove(absfile)
        return (ansistr)


if __name__ == '__main__':
    app.run()
