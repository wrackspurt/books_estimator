from flask import Flask, render_template, request
from get_data import get_genres
from dictionaries import genres_dict, emotions_dict
import text2emotion as te
import pandas as pd
import pickle

genres = get_genres()

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def get_info():
    return render_template('home.html', genresList=genres)


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
    if "None" in ug_list:
        ug_list.remove("None")
    """if len(book_desc) == 0:
            desc_error = 'please, enter the book description'
            print(desc_error)
        elif len(ug_list) == 0:
            genres_error = 'please, choose at least one genre'
            print(genres_error)"""
    if len(book_desc) == 0 or len(ug_list) == 0:
        enter_error = "It seems like you have not entered the book description and/or " +\
                      "you have not chosen at least one genre. Please, specify both " + \
                      "the book description and the genres to get the prediction."
        return render_template('home.html', enter_error=enter_error, genresList=genres)
    else:
        emotions = te.get_emotion(book_desc)
        if emotions['Angry'] + emotions['Fear'] + emotions['Happy'] + emotions['Sad'] + emotions['Surprise'] == 0.0:
            emo_error = "The book description is inapplicable. Please, enter another one and " +\
                        "do not forget to specify the genres again."
            return render_template('home.html', emo_error=emo_error, genresList=genres)
        else:
            emotions_dict['anger'].append(emotions['Angry'])
            emotions_dict['fear'].append(emotions['Fear'])
            emotions_dict['happiness'].append(emotions['Happy'])
            emotions_dict['sadness'].append(emotions['Sad'])
            emotions_dict['surprise'].append(emotions['Surprise'])
            print(emotions_dict)
            for u in ug_list:
                if u in genres_dict.keys():
                    genres_dict[u][0] += 1
            print(genres_dict)
            x_data = pd.DataFrame({**emotions_dict, **genres_dict})
            prediction = model.predict(x_data)
            print(prediction)
            result = round(prediction[0], 3)
            print(result)
            for e in emotions_dict.keys():
                emotions_dict[e].clear()
            for g in genres_dict.keys():
                if genres_dict[g][0] == 1:
                    genres_dict[g][0] -= 1
            return render_template('home.html', result=result, genresList=genres)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
