from flask import Flask, render_template, make_response, session, make_response, request
from werkzeug.utils import secure_filename  # Used for file uploads
import os
from os.path import join, dirname, realpath
import itinerary_module
import calendar_module

# from firebase_admin import firestore, credentials, initialize_app

# Firebase initializing
# cred = credentials.Certificate("serviceAccountKey.json")
# app = initialize_app(cred)
# db = firestore.client()
# Firebase initializing

app = Flask(__name__)
app.secret_key = "0f8b470adaa5ab09a365987d999730bdee4703110f72424a8c175b8a8d6a18b5"
# Files will be stored in a folder called uploads
UPLOAD_FOLDER = join(dirname(realpath(__file__)), "uploads")
ALLOWED_EXTENSIONS = {"jpg", "png", "mp3"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000  # Limits amount of memory to 16 MB


@app.route("/")
def index():
    template = render_template("index.html")
    response = make_response(template)
    # Create a cache to load faster
    response.headers["Cache-Control"] = "public, max-age=300, s-maxage=600"
    return response


@app.route("/suggest")
def suggest():
    return suggest.suggest()


@app.route("/itinerary", methods=["POST", "GET"])
def itinerary():
    if request.method == "POST":
        form = request.form
        name = form.get("name")
        schedule = itinerary_module.create_itinerary(name)

        template = render_template(
            "itinerary.html",
            schedule=schedule,
            show_calendar=True,
        )
        session["schedule"] = schedule
        response = make_response(template)
        response.headers["Cache-Control"] = "public, max-age=300, s-maxage=600"
        return response

    else:
        template = render_template("itinerary.html", show_calendar=False)
        response = make_response(template)
        response.headers["Cache-Control"] = "public, max-age=300, s-maxage=600"
        return response


@app.route("/get", methods=["GET"])
def get():
    if request.method == "GET":
        data = request.args.get("data")
        return data


@app.route("/calendar", methods=["POST"])
def calendar():
    if request.method == "POST":
        form = request.form
        date = form.get("date")
        print(date)
        schedule = session["schedule"]
        calendar_module.calendar_event(schedule, date)
        # Create a function to add this to the user's travel history
        return "Calendar created"

@app.route("/login")
def login():
    pass

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
    )
