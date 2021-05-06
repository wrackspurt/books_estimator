import pandas as pd
from sklearn.linear_model import ElasticNetCV
from sklearn.linear_model import ElasticNet
import pickle
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split


ds = pd.read_csv('bdata_dummies.csv')
columns = ds.columns.drop(labels=['book_title', 'book_authors', 'book_desc',
                                  'book_title', 'genres', 'emotion_index',
                                  'book_rating', 'book_rating_count',
                                  'book_review_count'])
X = ds[[c for c in columns]]
y = ds['book_rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
cv = KFold(n_splits=10, random_state=1, shuffle=True)
mdl_en_cv = ElasticNetCV(l1_ratio=[1, 0.5, 0.2, 0.3, 0.4, 0.01], n_alphas=100, cv=cv, n_jobs=-1).fit(X, y)
en_alpha = mdl_en_cv.alpha_
en_l1 = mdl_en_cv.l1_ratio_
# print(en_l1)
# print(en_alpha)

model = ElasticNet(alpha=en_alpha, l1_ratio=en_l1)
model.fit(X, y)
pickle.dump(model, open('model.pkl', 'wb'))
