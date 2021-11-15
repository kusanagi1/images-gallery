""" This is the main api code"""
import os
import requests
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv(dotenv_path=".env.local")
UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = os.environ.get("DEBUG") if os.environ.get("DEBUG") else False

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create .env.local file and insert UNSPLASH_KEY")

app = Flask(__name__)
app.config["DEBUG"] = DEBUG
CORS(app)


@app.route("/new-image")
def new_image():
    """This defines the endpoint function"""
    word = request.args.get("query")
    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + UNSPLASH_KEY}
    params = {"query": word}
    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)

    data = response.json()
    return data


# def hello():
#     return "Hello, World!"

# app.route("/")(hello)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2222)
