from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bird/<name>")
def bird(name):
    return render_template('user.html', name=name)

@app.route("/wiki")
def wiki():
    return redirect('http://wikipedia.org')

if __name__ == "__main__":
    app.run()
