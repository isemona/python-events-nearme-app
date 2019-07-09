from flask import Flask, flash, redirect, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)

# Normally, if you use an undefined variable in Jinja2, it fails silently.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "meet-python"

@app.route("/")
def hello():
    """Homepage"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)