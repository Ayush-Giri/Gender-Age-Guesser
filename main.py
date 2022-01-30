from flask import Flask, render_template
import requests

app = Flask(__name__)

genderize_api_endpoint = "https://api.genderize.io"
agify_api_endpoint = "https://api.agify.io"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/guess/<username>")
def guess(username):
    genderize_and_agify_parameters = {
        "name": username.title()
    }
    genderize_response = requests.get(url=genderize_api_endpoint, params=genderize_and_agify_parameters)
    genderize_result = genderize_response.json()["gender"]
    agify_response = requests.get(url=agify_api_endpoint, params=genderize_and_agify_parameters)
    agify_result = agify_response.json()["age"]
    return render_template("gender_age.html", name=username.title(), gender=genderize_result, age=agify_result)


if __name__ == "__main__":
    app.run(debug=True)
