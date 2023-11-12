from flask import Flask, render_template

app = Flask(__name__, template_folder="final_project/template")


@app.route('/')
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)