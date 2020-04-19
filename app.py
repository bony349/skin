from helper import *
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
   return "FUCK"


if __name__ == '__main__':
    app.run()

