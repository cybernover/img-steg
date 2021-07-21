import os
from flask import Flask, render_template

from modes.Text.text import text



UPLOAD_TEXT_FOLDER = 'modes\\Text\\static'
TEXT_CACHE_FOLDER = 'modes\\Text\\__pycache__'


app = Flask(__name__)
app.secret_key = "hello"

app.config['UPLOAD_TEXT_FOLDER'] = UPLOAD_TEXT_FOLDER
app.config['TEXT_CACHE_FOLDER'] = TEXT_CACHE_FOLDER

app.register_blueprint(text, url_prefix="/text")


@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)