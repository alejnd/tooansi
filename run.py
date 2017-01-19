from config import config
from flask import Flask, request
import magic
import png2ansi
import os

# example: curl -F "file=@sample.png"  localhost:5000/upload

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = os.urandom(24)

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files: return ('Error: No file given')
        
        file = request.files['file']
        absfile = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(absfile)

        # Check fileformat
        if magic.from_file(absfile, mime=True) !='image/png': return ('Error: file must be PNG image')

        ansistr = png2ansi.convert(absfile)
        os.remove(absfile)
        return (ansistr)


if __name__ == '__main__':
    app.run()