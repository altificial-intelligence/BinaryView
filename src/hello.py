from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    with open("out/counts/donaldtrump.txt") as fileHandler:
        for line in fileHandler:
            print line

    return "Hello world!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)