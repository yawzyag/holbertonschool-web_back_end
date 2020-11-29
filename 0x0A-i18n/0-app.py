#!/usr/bin/env python3
"""[basic flask app]
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    """[basic template]

    Returns:
        [type]: [template]
    """
    title = "Welcome to Holberton"
    hello = "Hello world"
    return render_template('0-index.html',
                           title=title, hello=hello)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
