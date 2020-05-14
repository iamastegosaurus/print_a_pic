from flask import Flask, render_template, url_for, request, redirect, flash
import os
import json 
from werkzeug.utils import secure_filename
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = path + '\\images'

def printapic(filename):
        with open(path + "\\settings.json", 'r+') as f:
            config = json.load(f)
            config['image'] = filename
            f.seek(0)
            json.dump(config, f)
            f.truncate()

        os.system("blender --background --python " + path + "\\printapic.py")
        with open(path + "\\settings.json") as f:
            config = json.load(f)
        return f"finished processing {config['image']} in {config['time']} seconds"

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        # t = datetime.now().date()

        if len(filename) > 13:
            filename = filename[0:10] + extension

        # filename = filename + '-' + str(t.month) + '-' + str(t.day) + extension

        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return printapic(filename)
        else:
            return render_template('index.html')

    return render_template('index.html')



if __name__ == "__main__":

    app.secret_key = 'super secret key'
    app.run(debug=True)

