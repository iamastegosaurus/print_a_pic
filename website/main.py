from flask import Flask, render_template, url_for, request, redirect
import os
import json 

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():

    # os.system("blender --background --python " + path + "\\printapic.py")
    # with open(path + "\\settings.json") as f:
    #     config = json.load(f)
    # return f"completed in {config['time']} seconds"

    if request.method == 'POST':
        filename = request.form['content']
        return filename
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

