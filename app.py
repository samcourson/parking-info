# app.py
from flask import Flask, render_template
from flask import send_from_directory
import os

app = Flask(__name__, static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'static'), filename)

if __name__ == '__main__':
    app.run(debug=True)

