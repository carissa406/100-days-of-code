from flask import Flask
import random

app = Flask(__name__)


@app.route("/") #decorator
def hello_world():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
            "<p>this is a paragraph</p>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

number = random.randint(0,9)

@app.route("/<int:usernumber>")
def guessed_number(usernumber):
    if usernumber > number:
        return "<h1 style= 'color:red'>Too high, try again!</h1>" \
                "<img src = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if usernumber < number:
        return "<h1 style= 'color:blue'> Too low, try again!</h1>" \
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style= 'color:green'>You're right! The number is: {number}</h1>" \
                "<img src = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug = True)