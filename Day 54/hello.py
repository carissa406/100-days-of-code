from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()

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