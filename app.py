from flask import (
    Flask,
    render_template,
    redirect,
    request
)
#import os
#import wordCounts as wc

app = Flask(__name__)

@app.route("/")
def main():
    return redirect('/index')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route('/test', methods = ['POST'])
def test():
    data = request.form['test']
    print("test data is " + data)
    return redirect('/')

"""
def hello_world():
    words = wc.classifyImages('bernie sanders', 10, 'face', 'y[1]')
    output = str()
    for word in words:
        output += word + " "
    return output
"""

if __name__ == '__main__':
    #app.run(port=33507)
    app.run()
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port)