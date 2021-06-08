from flask import Flask

app = Flask(__name__)

if(__name__=="__main__") :
    app.run()

def welcome() :
    return "Welcome to my App Server"