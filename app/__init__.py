#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from data import get_certificates

app = Flask(__name__)


@app.route("/certificates")
def certificates():
    certs = [item.serialize for item in get_certificates()]
    return jsonify(certs), 200


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
