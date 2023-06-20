from flask import Flask, render_template
import datetime as dt
import requests


app = Flask(__name__)


@app.route("/")
def home():
    c_name = "The Creator"
    current_year = dt.datetime.today().year
    return render_template("index.html", year=current_year, c_name=c_name)


@app.route("/guess/<name>")
def guess(name):
    agify_url = f"https://api.agify.io/?name={name}"
    genderize_url = f"https://api.genderize.io/?name={name}"

    age = requests.get(agify_url).json()["age"]
    gender = requests.get(genderize_url).json()["gender"]

    return render_template("guess.html", gender=gender,age=age, name=name)


if __name__ == "__main__":
    app.run(debug=True)