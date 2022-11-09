"""
Webapp that can return the closest MBTA stop and whether it is wheelchair accessible.
"""

from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=["GET", "POST"])
def place_name():
    if request.method == "POST":
        place = request.form["place"]
        stop, wheelchair = find_stop_near(place)
        return render_template("results.html", place = stop,wheelchair=wheelchair) 
    else:      
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
