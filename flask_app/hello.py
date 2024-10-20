# Describe where/path and what(in this cas it is a class of Flask): importing.
import os
from flask import Flask, render_template

print(f"Flask environment is set to: {os.getenv.__get__('FLASK_ENV')}")

app = Flask(__name__)
@app.route("/")
def hello_world():
    name = "Trevor"
    return render_template('index.html', name=name)

@app.route("/name/<name>")
def hello_name(name):
    return f"Hello {name}" 

if __name__ == "__main__":
    app.run(debug=True)

# To run a file in the terminal in a Flask app. 
# FLASK_APP=hello.py flask run

# Flask handles routing for web apps.
# Computer sends request...
# ...Server sends response.