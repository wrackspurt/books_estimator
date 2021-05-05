from flask import Flask, render_template, redirect, url_for, request
from get_data import get_genres

GENRES = get_genres()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html', genresList=GENRES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)