#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from data import get_certificates, get_works

app = Flask(__name__)


@app.route("/certificates")
def show_certificates():
    certificates = [item.serialize for item in get_certificates()]
    return jsonify(certificates), 200


@app.route("/works")
def show_works():
    works = [item.serialize for item in get_works()]
    return jsonify(works), 200


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
