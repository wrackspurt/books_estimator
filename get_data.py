import pandas as pd


def get_genres():
    ds = pd.read_csv('bdata_dummies.csv')
    titles = []
    columns = ds.columns.drop(labels=['book_title', 'book_authors', 'book_desc',
                                      'book_title', 'genres', 'emotion_index',
                                      'book_rating', 'book_rating_count',
                                      'book_review_count', 'anger', 'fear',
                                      'happiness', 'sadness', 'surprise'])
    for c in columns:
        titles.append(c)
    return titles
