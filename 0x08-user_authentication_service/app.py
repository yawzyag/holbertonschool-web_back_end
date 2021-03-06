#!/usr/bin/env python3
"""
Route module for the API
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth
app = Flask(__name__)

app.url_map.strict_slashes = False
AUTH = Auth()


@app.route('/')
def hello_world():
    """[hello world flask]

    Returns:
        [type]: [json message]
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
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


@app.route('/sessions', methods=['POST'])
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
                out.set_cookie("session_id", session_id)
                return out
        except Exception as e:
            abort(401)
    abort(401)


@app.route('/sessions', methods=['DELETE'])
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


@app.route('/profile', methods=['GET'])
def profile():
    """[profile]

    Returns:
        str: [description]
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if (user):
        AUTH.destroy_session(user.id)
        return jsonify({"email": user.email})
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token() -> str:
    """[reset token]

    Returns:
        str: [token]
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
            token = AUTH.get_reset_password_token(email)
            return jsonify({"email": email,
                            "reset_token": token}), 200
        except ValueError:
            abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password() -> str:
    """[summary]

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
            new_password = rj.get("new_password")
            token = rj.get("reset_token")
            AUTH.update_password(token, new_password)
            return jsonify({"email": email,
                            "message": "Password updated"})
        except ValueError:
            abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
