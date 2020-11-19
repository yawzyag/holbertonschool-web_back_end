#!/usr/bin/env python3
"""
Main file
"""
import requests

headers = {'User-Agent': 'Mozilla/5.0'}
url = "http://localhost:5000"
session = requests.Session()


def register_user(email: str, password: str) -> None:
    payload = {'email': email, 'password': password}
    url_req = url + '/users'
    response = session.post(url_req,
                            headers=headers, data=payload)
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    payload = {'email': email, 'password': password}
    url_req = url + '/sessions'
    response = session.post(url_req,
                            headers=headers, data=payload)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    payload = {'email': email, 'password': password}
    url_req = url + '/sessions'
    response = session.post(url_req,
                            headers=headers, data=payload)
    cookies = session.cookies.get_dict()
    assert response.status_code == 200
    return cookies.get('session_id')


def profile_unlogged() -> None:
    cookies = {}
    url_req = url + '/profile'
    response = session.get(url_req,
                           headers=headers, cookies=cookies)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    cookies = {'session_id': session_id}
    url_req = url + '/profile'
    response = session.get(url_req,
                           headers=headers, cookies=cookies)
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    url_req = url + '/sessions'
    cookies = {'session_id': session_id}
    response = session.delete(url_req,
                              headers=headers, cookies=cookies)


def reset_password_token(email: str) -> str:
    payload = {'email': email}
    url_req = url + '/reset_password'
    response = session.post(url_req,
                            headers=headers, data=payload)
    assert response.status_code == 200
    return response.json().get('reset_token')


def update_password(email: str, reset_token: str, new_password: str) -> None:
    payload = {'email': email, 'reset_token': reset_token,
               'new_password': new_password}
    url_req = url + '/reset_password'
    response = session.put(url_req,
                           headers=headers, data=payload)
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
