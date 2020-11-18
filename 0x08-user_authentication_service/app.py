#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)

AUTH = Auth()


@app.route('/')
def hello_world():
    """[hello world flask]

    Returns:
        [type]: [json message]
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """[create user]

    Returns:
        str: [description]
    """
    rj = None
    error_msg = None
    try:
        rj = request.form
    except Exception as e:
        rj = None

    if error_msg is None and rj:
        try:
            email = rj.get("email")
            password = rj.get("password")
            AUTH.register_user(email, password)
            return jsonify({"email": email,
                            "message": "user created"}), 200
        except Exception as e:
            error_msg = {"message": "email already registered"}
    return jsonify(error_msg), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
