#!/usr/bin/env python3
""" Module of sesion auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from api.v1.app import auth
import os
from flask import session


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    email = request.form.get("email")
    if (not email):
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password")
    if (not password):
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})

    if (not user):
        return jsonify({"error": "no user found for this email"}), 404
    if (not user[0].is_valid_password(password)):
        return jsonify({"error": "wrong password"}), 401

    sesion_id = auth.create_session(user[0].id)
    sesion_name = os.getenv("SESSION_NAME")
    out = jsonify(user[0].to_json())
    out.set_cookie(sesion_name, sesion_id)
    return out


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def delete_session() -> str:
    """[delete session endpoint]

    Returns:
        str: [empty if delte session]
    """
    state = auth.destroy_session(request)
    if (state):
        return jsonify({}), 200
    abort(404)
