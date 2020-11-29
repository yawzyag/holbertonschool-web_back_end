#!/usr/bin/env python3
"""[basic flask app]
"""
from flask import Flask, g, request, render_template
from flask_babel import Babel
app = Flask(__name__)
app.url_map.strict_slashes = False


class Config():
    """[config for babel]

    Returns:
        [type]: [config]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """[get local lng]

    Returns:
        [type]: [local lng]
    """
    locale = request.args.get('locale')
    if (locale in Config.LANGUAGES):
        return locale
    user = getattr(g, 'user', None)
    if (user):
        locale = user.get('locale')
        if (locale in Config.LANGUAGES):
            return locale
    locale_header = request.headers.get('locale')
    if (locale_header in Config.LANGUAGES):
        return locale_header

    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user(login_as: str):
    """[get user]

    Args:
        id (str): [description]

    Returns:
        str: [description]
    """
    if (login_as):
        user_d = users.get(int(login_as))
        if (user_d):
            return user_d
    return None


@app.before_request
def before_request_func():
    id_u = request.args.get('login_as')
    g.user = get_user(id_u)


@app.route('/')
def hello_world():
    """[basic template]

    Returns:
        [type]: [template]
    """
    user = getattr(g, 'user', None)
    return render_template('6-index.html', user=user)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
