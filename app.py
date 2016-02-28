from flask import (
    Flask,
    render_template,
    redirect,
    request
)
import json

from src import googleSearch, clarifaiClassify

app = Flask(__name__)

@app.route("/")
def main():
    return redirect('/query')

@app.route("/query")
def query():
    return render_template('query.html')

@app.route('/classify', methods = ['POST'])
def classify():
    query = request.form['query']
    urls = googleSearch.getUrls(query, 10, 'face', 'y[2]')
    firstImage = urls[0]
    words = clarifaiClassify.classifyUrls(urls)
    jsonWords = json.dumps(words)

    return render_template('classify.html', person=query, image=firstImage, data=jsonWords)

if __name__ == '__main__':
    app.debug = True
    app.run()