#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, g
from data import get_certificates, get_works, User, get_user_by_id, get_skills
from data import get_experience
from flask_httpauth import HTTPBasicAuth
from settings import BASE_DIR

# define global variables
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(_login, password):
    """
       User verification
       :param _login: (str)
       :param password: (str)
       :return bool:
    """
    user_id = User.verify_auth_token(_login)
    if user_id:
        user = get_user_by_id(user_id)
        if not user.verify_password(password):
            return False
    else:
        return False
    g.user = user
    return True


@app.route("/")
def home():
    """
    Read and return index HTML file
    :return String:
    """
    path = "%s/%s" % (BASE_DIR, "index.html")
    with open(path, "r+") as f:
        html = f.read()
    return html


@app.route("/certificates")
def show_certificates():
    """
    Return all certificates (JSON format)
    :return String: (JSON)
    """
    certificates = [item.serialize for item in get_certificates()]
    return jsonify(certificates), 200


@app.route("/works")
def show_works():
    works = [item.serialize for item in get_works()]
    return jsonify(works), 200


@app.route("/skills")
def show_skills():
    """
    Return all skills with categories (JSON format)
    :return String: (JSON)
    """
    skills = [item.serialize for item in get_skills()]
    return jsonify(skills), 200


@app.route("/experience")
def show_experience():
    experience = [item.serialize for item in get_experience()]
    return jsonify(experience), 200


@app.route("/token")
@auth.login_required
def get_auth_token():
    """
    Return auth token
    :return string: JSON
    """
    return jsonify({'token': g.user.generate_auth_token().decode('ascii'),
                    'uid': g.user.id,
                    'first_name': g.user.first_name,
                    'last_name': g.user.last_name,
                    'status': g.user.status,
                    'role': g.user.role,
                    'email': g.user.email})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
