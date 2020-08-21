import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


filename = '../data/cannabis.csv'
df = pd.read_csv(filename)
tfidf = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1, 2),
    max_df=.90,
    min_df=10,
)
dtm = tfidf.fit_transform(
    df['Name'] + '. ' + df['Description'] + ' ' + df['Effects'] + ' ' + df['Flavors']
)
dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
pickle.dump(tfidf, open('tfidf.pickle', 'wb'))  # TFIDF
nearest_one = NearestNeighbors(n_neighbors=1, algorithm='kd_tree', n_jobs=-1)
nearest_one.fit(dtm)
pickle.dump(nearest_one, open('nearest.pickle', 'wb'))  # Nearest
