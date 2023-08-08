from flask import Flask, render_template, request
import pyshorteners
import os
from pyshorteners import Shortener
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    res=longUrl=request.form['longUrl']
    return shortener(res) 


def shortener(url):
    #TinyURL shortener service
    global short_url
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    print("The Shortened URL is: " + short_url)
    return short_url


if __name__ == "__main__":
    app.run()
