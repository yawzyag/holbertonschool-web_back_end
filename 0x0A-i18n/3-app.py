#!/usr/bin/env python3
"""[basic flask app]
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _
app = Flask(__name__)


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


@babel.localeselector
def get_locale():
    """[get local lng]

    Returns:
        [type]: [local lng]
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def hello_world():
    """[basic template]

    Returns:
        [type]: [template]
    """
    home_title = _("home_title")
    home_header = _("home_header")
    return render_template('3-index.html',
                           home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="6090")
