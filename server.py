""" Server for Met App."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
import requests
import json
from jinja2 import StrictUndefined
import random
import art

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def show_art():
    dept_id = art.find_dept("Egyptian Art")
    objects = art.find_objs_in_dept(dept_id)
    artwork_display = art.ten_objs(objects)

    return render_template('index.html', display=artwork_display)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
