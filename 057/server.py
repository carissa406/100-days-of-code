from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route("/") #decorator
def hello_world():
    random_number = random.randint(1,10)
    current_year = datetime.date.today().year
    return render_template('index.html', num=random_number, year=current_year) #keyword arguments

@app.route("/guess/<their_name>") #variable with <> can be used later
def greet(their_name):
    response = requests.get(url=f"https://api.agify.io?name={their_name}")
    response.raise_for_status()
    data = response.json()

    their_age = str(data["age"])

    response = requests.get(url=f"https://api.genderize.io?name={their_name}")
    response.raise_for_status()
    data = response.json()
    
    their_gender = str(data["gender"])

    their_name = str(data["name"])

    return render_template('name.html', name=their_name, age=their_age, gender=their_gender)
    #f"{their_name} {their_age} {their_gender}"


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template('blog.html', posts = all_posts)


if __name__ == "__main__":
    #debug true to reload server automatically when we save the file
    app.run(debug = True) 

#put code inside {{}} to make flask return the actual python code "templating language"