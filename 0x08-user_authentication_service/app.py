#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """[login]

    Returns:
        str: [json payload]
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
            valid = AUTH.valid_login(email, password)
            if (valid):
                session_id = AUTH.create_session(email)
                out = jsonify({"email": email, "message": "logged in"})
                out.set_cookie("sesion_id", session_id)
                return out
        except Exception as e:
            abort(401)
    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """[logout user]

    Returns:
        str: [state]
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if (user):
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """[profile]

    Returns:
        str: [description]
    """
    session_id = request.cookies.get('session_id')
    try:
        user = AUTH.get_user_from_session_id(session_id)
        if (user):
            AUTH.destroy_session(user.id)
            return jsonify({"email": user.email}), 200
    except Exception:
        pass
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
