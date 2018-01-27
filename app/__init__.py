from flask import Flask
from settings import db

app = Flask(__name__)


@app.route("/certificates")
def certificates():
    return ""
