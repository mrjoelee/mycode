#!/usr/bin/python3
"""
Joe | joe.lee@tlgcohort.com
Flask Project
"""

# python3 -m pip install flask
from flask import Flask
from flask import redirect
from flask import url_for


# create flask app instance
app = Flask(__name__)

@app.route("/admin")
def hello_admin():
    return "Hello Admin"


if __name__ =="__main__":
    app.run(host="0.0.0.0", port=2224)




