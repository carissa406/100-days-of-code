from flask import Flask

app = Flask(__name__)


@app.route("/") #decorator
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>this is a paragraph</p>" \
            "<img src='https://media.giphy.com/media/TEkr9oBZ57KFmMWScZ/giphy.gif'>"


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return 'Byebye'

#<path:username> = Angela/12
#<int:number>

@app.route("/username/<name>") #variable with <> can be used later
def greet(name):
    return f'Hello {name}!'



if __name__ == "__main__":
    app.run(debug = True) #debug true to reload server automatically when we save the file




#positional arguments
    #keyword arguments

inputs = eval(input())
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args):
    print(f"You called {function.__name__}{args}")
    print(f"It returned: {function(args[0],args[1],args[2])}")
  return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
  return a * b * c

a_function(inputs[0], inputs[1], inputs[2])















#functions are first class objects, can be passed as arguments
#nested functions
#functions can be returned from other functions
    
##Python Decorator
import time
def delay_decorator(function):
    def wrapper_function():
        time.sleep(1)
        #do something before
        function()
        #do smoethng after
    return wrapper_function

@delay_decorator
def say_hello():
    print("hello")