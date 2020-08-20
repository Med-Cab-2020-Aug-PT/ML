import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from time import time
import pickle


print("Loading Data...")
start = time()
filename = '../data/cannabis.csv'
df = pd.read_csv(filename)
print(f"Time taken: {time() - start:.3f} sec.\n")

print("Loading Spacy...")
start = time()
nlp = spacy.load("en_core_web_lg")
print(f"Time taken: {time() - start:.3f} sec.\n")


def tokenize(document):
    doc = nlp(document)
    return [
        token.lemma_.strip() for token in doc
        if not token.is_stop and not token.is_punct
    ]


print("Fitting TFIDF...")
start = time()
tfidf = TfidfVectorizer(
    stop_words='english',
    tokenizer=tokenize,
    ngram_range=(1, 2),
    max_df=.95,
    min_df=5,
)
dtm = tfidf.fit_transform(
    df['Name'] + '. ' + df['Description'] + ' ' + df['Effects'] + ' ' + df['Flavors']
)
dtm = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
print(f"Time taken: {time() - start:.3f} sec.\n")
pickle.dump(tfidf, open('tfidf.pickle', 'wb'))

print("Fitting NearestNeighbor...")
start = time()
nearest_one = NearestNeighbors(n_neighbors=1, algorithm='kd_tree', n_jobs=-1)
nearest_one.fit(dtm)
print(f"Time taken: {time() - start:.3f} sec.\n")
pickle.dump(nearest_one, open('nearest.pickle', 'wb'))

print("Cleaning up...")
start = time()
data = df.to_dict(orient='records')
for strain in data:
    strain['Effects'] = strain['Effects'].split(',')
    strain['Flavors'] = strain['Flavors'].split(',')
    strain['Nearest'] = strain['Nearest'].split(',')
print(f"Time taken: {time() - start:.3f} sec.\n")


def recommend(user_input):
    rec = nearest_one.kneighbors(
        tfidf.transform([user_input]).todense()
    )
    return dict(data[rec[1][0][0]])


if __name__ == '__main__':
    user_string = "I have a headache"
    print(f"Making Recommendation for '{user_string}'...")
    start = time()
    print(recommend(user_string))
    print(f"Time taken: {time() - start:.3f} sec.\n")
