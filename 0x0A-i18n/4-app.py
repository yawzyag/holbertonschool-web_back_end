#!/usr/bin/env python3
"""[basic flask app]
"""
from flask import Flask, request, render_template
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


@babel.localeselector
def get_locale():
    """[get local lng]

    Returns:
        [type]: [local lng]
    """
    locale = request.args.get('locale')
    if (locale and locale in Config.LANGUAGES):
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def hello_world():
    """[basic template]

    Returns:
        [type]: [template]
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
