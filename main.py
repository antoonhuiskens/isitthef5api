from bs4 import BeautifulSoup
from flask import Flask, jsonify

import requests

app = Flask(__name__)

@app.route("/")
def is_it_the_f5():
    g = requests.get('https://isitthef5.com/')
    s = BeautifulSoup(g.text, features="html.parser")
    r = dict()
    r['blame_f5']= s.html.body.get_text()
    return jsonify(r)