from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/find")
def tracuu():
    userText = request.args.get('query')
    return str(userText)

if __name__ == "__main__":
    app.run()
