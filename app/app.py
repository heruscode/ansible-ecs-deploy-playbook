import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def main_route():
   return "Simple flask app running!"

if __name__ == '__main__':
    app.run("0.0.0.0", port=80)