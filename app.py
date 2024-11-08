from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! This is a basic Flask app...."

@app.route('/hello')
def hello():
    return "Hello, no World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
