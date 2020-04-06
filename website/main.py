from flask import Flask, render_template, url_for, request, redirect
import os
import json 

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        filename = request.form['content']

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

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

