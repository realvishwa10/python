from flask import Flask

app = Flask(__name__)
print(__name__)


def make_bold(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/bye")
@make_bold
@make_emphasis
def bye():
    return "Bye!"

if __name__ == '__main__':
    # run app in debug mode
    app.run(debug=True)