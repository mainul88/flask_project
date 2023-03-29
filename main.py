from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def great_name():
    return render_template("user.html")


if __name__ == '__main__':
    app.run(debug=True)
