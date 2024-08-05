from flask import Flask, render_template, make_response, session, make_response, request
from werkzeug.utils import secure_filename # Used for file uploads
import os
from os.path import join, dirname, realpath
# from firebase_admin import firestore, credentials, initialize_app

# Firebase initializing
# cred = credentials.Certificate("serviceAccountKey.json")
# app = initialize_app(cred)
# db = firestore.client()
# Firebase initializing

app = Flask(__name__)
app.secret_key = None # Create your own secret key using this command: python -c 'import secrets; print(secrets.token_hex())'
# Files will be stored in a folder called uploads
UPLOAD_FOLDER = join(dirname(realpath(__file__)), "uploads")
ALLOWED_EXTENSIONS = {"jpg", "png", "mp3"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000 # Limits amount of memory to 16 MB

@app.route("/")
def index():

    template = render_template("index.html") # If you are rendering template variables, just add them as a parameter, eg. variable = "something"
    response = make_response(template)
    response.headers["Cache-Control"] = "public, max-age=300, s-maxage=600" # Create a cache to load faster
    return response

# Example of url GET method request
@app.route("/get", methods=["GET"])
def get():
    if request.method == "GET":
        data = request.args.get("data")
        return data

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
