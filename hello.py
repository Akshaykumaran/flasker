from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    stuff=" This is <strong>Bold </strong>"
    return render_template('index.html')

@app.route("/user/<name>")
def username(name):
    return render_template('user.html',name=name)


if __name__=="__main__":
    app.run(debug=True)