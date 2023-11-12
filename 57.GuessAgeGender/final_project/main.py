from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/a557423de18f51f4678f").json()
data_list = []
for data in posts:
    post_item = (data["id"], data["title"], data["subtitle"], data["body"])
    data_list.append(post_item)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", converted_data=data_list)

if __name__ == "__main__":
    app.run(debug=True)
