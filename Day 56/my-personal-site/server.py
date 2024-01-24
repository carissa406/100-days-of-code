from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") #decorator
def hello_world():
    return render_template('index.html')



if __name__ == "__main__":
    #debug true to reload server automatically when we save the file
    app.run(debug = True) 
