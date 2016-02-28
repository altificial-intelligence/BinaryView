from flask import (
    Flask,
    render_template,
    redirect,
    request
)

import clarifaiClassify
from src import googleSearch

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

    """
    words = wc.classifyImages('bernie sanders', 10, 'face', 'y[1]')
    output = str()
    for word in words:
        output += word + " "
    print words
    """

    return render_template('classify.html', image=firstImage, data=words)

if __name__ == '__main__':
    app.debug = True
    app.run()