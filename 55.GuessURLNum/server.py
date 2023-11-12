from flask import Flask
import random

app = Flask(__name__)
random_num = random.randint(0, 9)
print(random_num)


@app.route('/')
def home_page():
    return "<h1 style='text-align:center'>Guess a number between 0 and 9</h1>"\
            "<center><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/></center>"


@app.route('/<guess_num>')
def correct_guess(guess_num):
    if int(guess_num) == random_num:
        return "<h2 style='text-align:center';'color:Green';>You found me!</b>"\
               "<center><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/></center>"
    elif int(guess_num) > random_num:
        return "<h2 style='text-align:center';'color:Purple';>Too High! Try again</b>" \
               "<center><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/></center>"
    elif int(guess_num) < random_num:
        return "<h2 style='text-align:center';'color:Red';>Too Low! Try again</b>" \
               "<center><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/></center>"

if __name__ == "__main__":
    app.run(debug=True)