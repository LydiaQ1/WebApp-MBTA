"""
Webapp that can return the closest MBTA stop and whether it is wheelchair accessible.
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/place_name/', methods=["GET", "POST"])
def place_name():
    if request.method == "POST":
        place_name = request.form["placename"]
        return render_template("index.html", place_name)

    return render_template("index.html")

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True)
