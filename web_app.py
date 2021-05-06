from flask import Flask, render_template, redirect, url_for, request
from get_data import get_genres
from dictionaries import genres_dict, emotions_dict
import text2emotion as te
import pandas as pd
import pickle

GENRES = get_genres()
GENRES_DICT = genres_dict
EMOTIONS_DICT = emotions_dict

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def get_info():
    return render_template('home.html', genresList=GENRES)


@app.route('/', methods=['GET', 'POST'])
def post_results():
    book_desc = str(request.form.get('description'))
    g_list = list()
    g_list.append(str(request.form.get('genreChoice1')))
    g_list.append(str(request.form.get('genreChoice2')))
    g_list.append(str(request.form.get('genreChoice3')))
    g_list.append(str(request.form.get('genreChoice4')))
    g_list.append(str(request.form.get('genreChoice5')))
    g_list.append(str(request.form.get('genreChoice6')))
    g_list.append(str(request.form.get('genreChoice7')))
    g_list.append(str(request.form.get('genreChoice8')))
    g_list.append(str(request.form.get('genreChoice9')))
    g_list.append(str(request.form.get('genreChoice10')))
    g_list.append(str(request.form.get('genreChoice11')))
    g_list.append(str(request.form.get('genreChoice12')))
    g_list.append(str(request.form.get('genreChoice13')))
    g_list.append(str(request.form.get('genreChoice14')))
    g_list.append(str(request.form.get('genreChoice15')))
    g_set = set(g_list)
    ug_list = list(g_set)
    if len(book_desc) == 0:
        desc_error = 'please, enter the book description'
        print(desc_error)
    if "None" in ug_list:
        ug_list.remove("None")
    if len(ug_list) == 0:
        genres_error = 'please, choose at least one genre'
        print(genres_error)
    print(ug_list)
    emotions = te.get_emotion(book_desc)
    if emotions['Angry'] + emotions['Fear'] + emotions['Happy'] + emotions['Sad'] + emotions['Surprise'] == 0.0:
        emo_error = 'the book description is inapplicable. please, enter another one'
        print(emo_error)
    EMOTIONS_DICT['anger'].append(emotions['Angry'])
    EMOTIONS_DICT['fear'].append(emotions['Fear'])
    EMOTIONS_DICT['happiness'].append(emotions['Happy'])
    EMOTIONS_DICT['sadness'].append(emotions['Sad'])
    EMOTIONS_DICT['surprise'].append(emotions['Surprise'])
    print(EMOTIONS_DICT)
    for u in ug_list:
        if u in GENRES_DICT.keys():
            GENRES_DICT[u][0] += 1
    print(GENRES_DICT)
    x_data = pd.DataFrame({**EMOTIONS_DICT, **GENRES_DICT})
    prediction = model.predict(x_data)
    print(prediction)
    return render_template('home.html', genresList=GENRES)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
