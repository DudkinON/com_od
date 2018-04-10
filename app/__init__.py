#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, g, make_response
from data import get_certificates, get_works, User, get_user_by_id, get_skills
from data import get_experience, get_info, get_education, get_social
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
    res = make_response(jsonify(works))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route("/skills")
def show_skills():
    """
    Return all skills with categories (JSON format)
    :return String: (JSON)
    """

    skills = [item.serialize for item in get_skills()]
    res = make_response(jsonify(skills))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route("/experience")
def show_experience():
    """
    Return experience work places (JSON format)
    :return String: (JSON)
    """
    experience = [item.serialize for item in get_experience()]
    res = make_response(jsonify(experience))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route("/info")
def show_info():
    """
    Return user info (JSON format)
    :return String: (JSON)
    """
    info = [item.serialize for item in get_info()]
    res = make_response(jsonify(info))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route("/education")
def show_education():
    """
    Return education info (JSON format)
    :return String: (JSON)
    """
    info = [item.serialize for item in get_education()]
    res = make_response(jsonify(info))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route("/social")
def show_social():
    """
    Return list of social networks and contacts (JSON format)
    :return String: (JSON)
    """
    info = [item.serialize for item in get_social()]
    res = make_response(jsonify(info))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


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
