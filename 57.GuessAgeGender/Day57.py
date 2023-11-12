from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__, template_folder='template/')


@app.route('/')
def home_page():
    current_year = datetime.now().year
    my_name = "Ghost"
    return render_template("index.html", year=current_year, user_name=my_name)


@app.route('/guess/<guess_name>')
def name_guess(guess_name):
    import requests
    gender_url = 'https://api.genderize.io'
    gender_params = {"name": guess_name}
    gender_response = requests.get(url=gender_url, params=gender_params)
    gender_data = gender_response.json()
    print(gender_data)
    gender = gender_data["gender"]

    age_url = 'https://api.agify.io'
    age_params = {"name": guess_name}
    age_response = requests.get(url=age_url, params=age_params)
    age_data = age_response.json()
    age = age_data["age"]

    return render_template("guess_index.html", name=guess_name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)