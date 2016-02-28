from flask import (
    Flask,
    render_template,
    redirect,
    request
)
#import wordCounts as wc

app = Flask(__name__)

@app.route("/")
def main():
    return redirect('/query')

@app.route("/query")
def index():
    return render_template('query.html')

@app.route('/classify', methods = ['POST'])
def test():
    data = request.form['test']

    """
    words = wc.classifyImages('bernie sanders', 10, 'face', 'y[1]')
    output = str()
    for word in words:
        output += word + " "
    print words
    """

    return render_template('classify.html', test=data)


if __name__ == '__main__':
    app.run()